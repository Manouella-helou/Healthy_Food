import streamlit as st
from datetime import datetime
import os

# BMI Calculator Function
def calculate_bmi(weight, height):
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

# Complete recipes dictionary
recipes = {
    'Burgers': {
        'description': 'A healthier burger with a lean beef or plant-based patty, served on a whole grain bun and topped with fresh veggies.',
        'ingredients': [
            'Lean beef or plant-based patty', 'Whole grain buns', 'Lettuce', 
            'Tomato', 'Onion', 'Avocado', 'Mustard'
        ],
        'preparation': [
            'Season the patty with salt and pepper.',
            'Grill over medium heat for 3-4 minutes per side.',
            'Toast the whole grain buns.',
            'Assemble the burger with the patty, lettuce, tomato, onion, and avocado.',
            'Add mustard or preferred sauce.'
        ],
        'nutritional_info': 'Approx. 350 calories. Rich in protein and fiber.',
        'tags': ['Vegetarian', 'Vegan', 'Gluten-Free']
    },
    'Pizza': {
        'description': 'A delicious pizza with a whole wheat crust, topped with low-fat cheese and fresh vegetables.',
        'ingredients': [
            'Whole wheat pizza dough', 'Low-fat mozzarella cheese', 'Tomato sauce', 
            'Bell peppers', 'Onions', 'Mushrooms'
        ],
        'preparation': [
            'Preheat oven to 425°F.',
            'Roll out dough, apply tomato sauce.',
            'Add cheese and vegetable toppings.',
            'Bake for 15-20 minutes until crust is crispy.'
        ],
        'nutritional_info': 'About 250 calories per slice. High in fiber and vitamins.',
        'tags': ['Vegetarian', 'Vegan', 'Gluten-Free']
    },
    'Fries': {
        'description': 'Crispy and flavorful oven-baked sweet potato fries, seasoned with a blend of spices.',
        'ingredients': [
            'Sweet potatoes', 'Olive oil', 'Paprika', 'Garlic powder', 
            'Onion powder', 'Salt', 'Black pepper'
        ],
        'preparation': [
            'Preheat the oven to 425°F (220°C).',
            'Wash and peel the sweet potatoes, cutting them into thin fry shapes.',
            'Toss the fries with olive oil, paprika, garlic powder, onion powder, salt, and black pepper.',
            'Spread in a single layer on a baking sheet.',
            'Bake for 20-25 minutes, flipping halfway, until golden and crispy.',
            'Serve with your choice of dipping sauce.'
        ],
        'nutritional_info': 'Approximately 200 calories per serving. Rich in dietary fiber and vitamins A and C.',
        'tags': ['Vegetarian', 'Vegan', 'Gluten-Free']
    },
    'Fried Chicken': {
        'description': 'Crispy oven-baked chicken with a flavorful almond flour coating, offering a healthier version of the classic fried chicken.',
        'ingredients': [
            'Chicken breasts or thighs', 'Almond flour', 'Paprika', 
            'Garlic powder', 'Egg', 'Salt', 'Pepper'
        ],
        'preparation': [
            'Preheat the oven to 375°F (190°C) and line a baking sheet with parchment paper.',
            'Mix almond flour, paprika, garlic powder, salt, and pepper in a bowl.',
            'Beat the egg in another bowl.',
            'Dip chicken pieces in egg, then coat with almond flour mixture.',
            'Place on the baking sheet and bake for 25-30 minutes until golden and crispy.',
            'Let it cool before serving.'
        ],
        'nutritional_info': 'Approx. 300 calories per serving. High in protein and lower in carbs.',
        'tags': ['Gluten-Free']
    },
    'Noodles': {
        'description': 'Stir-fried whole grain or zucchini noodles with a mix of colorful veggies and lean protein, seasoned with light soy sauce and spices.',
        'ingredients': [
            'Whole grain or zucchini noodles', 'Choice of protein (chicken, shrimp, tofu)', 
            'Mixed vegetables (bell peppers, broccoli, carrots)', 'Soy sauce', 'Garlic', 
            'Ginger', 'Olive oil'
        ],
        'preparation': [
            'Prepare the noodles as per package instructions; for zucchini noodles, spiralize and set aside.',
            'Heat olive oil in a pan, add minced garlic and ginger, and sauté.',
            'Add the protein and cook until done. Then add the vegetables and stir-fry.',
            'Mix in the noodles and soy sauce, stir-fry for a few more minutes.',
            'Serve hot, garnished with herbs or sesame seeds.'
        ],
        'nutritional_info': 'Varies based on ingredients. Generally rich in fiber and nutrients.',
        'tags': ['Vegetarian', 'Vegan', 'Gluten-Free']
    },
    'Fried Shrimps': {
        'description': 'Lightly seasoned and baked or grilled shrimps, a delicious and healthier alternative to traditional fried shrimps.',
        'ingredients': [
            'Shrimps', 'Olive oil', 'Lemon juice', 'Garlic', 
            'Paprika', 'Salt', 'Pepper'
        ],
        'preparation': [
            'Marinate shrimps in olive oil, lemon juice, minced garlic, paprika, salt, and pepper.',
            'Let them marinate for 15-20 minutes in the refrigerator.',
            'Preheat the oven or grill to medium-high heat.',
            'Cook the shrimps for 2-3 minutes on each side until pink and cooked through.',
            'Serve hot with a side of vegetables or a salad.'
        ],
        'nutritional_info': 'Approx. 150-200 calories per serving. Rich in protein and omega-3 fatty acids.',
        'tags': ['Gluten-Free']
    },
    'Hotdogs': {
        'description': 'A healthier version of classic hotdogs, using lean chicken or turkey sausages and whole grain buns, topped with fresh and flavorful condiments.',
        'ingredients': [
            'Lean chicken or turkey sausages', 'Whole grain hotdog buns', 'Sauerkraut', 
            'Mustard', 'Ketchup', 'Diced onions', 'Sliced pickles'
        ],
        'preparation': [
            'Grill the sausages over medium heat until cooked thoroughly.',
            'Lightly toast the whole grain hotdog buns on the grill or in the oven.',
            'Place the cooked sausages in the buns.',
            'Top with sauerkraut, mustard, ketchup, diced onions, and sliced pickles.',
            'Serve immediately, accompanied with a side salad or grilled vegetables.'
        ],
        'nutritional_info': 'Approx. 250-300 calories per serving, depending on the toppings. Rich in protein and lower in saturated fats.',
        'tags': ['Gluten-Free']
    },
}

def display_recipe(recipe_name):
    if recipe_name in recipes:
        recipe = recipes[recipe_name]
        print(f"Recipe: {recipe_name}\n")
        print(f"Description: {recipe['description']}\n")
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(f"  {ingredient}")
        print("\nPreparation Steps:")
        for step in recipe['preparation']:
            print(f"  {step}")
        print(f"\nNutritional Information: {recipe['nutritional_info']}")
        print(f"Tags: {', '.join(recipe['tags'])}\n")
    else:
        print(f"Recipe '{recipe_name}' not found.")

# Sample data for nutritionists
nutritionists = {
    "Dr. Chekri Khalife": {
        "specialization": "Sports Nutrition",
        "contact": "ChekriKhalife@nutriswap.com",
        "image": "chekri.jpg",
        "availability": ["Monday - 10am to 4pm", "Wednesday - 12pm to 6pm"],
        "bio": "Dr. Chekri specializes in sports nutrition and diet planning for athletes."
    },
    "Charbel Daou, RD": {
        "specialization": "Clinical Dietetics",
        "contact": "CharbelDaou@nutriswap.com",
        "image": "Charbel.jpg",
        "availability": ["Tuesday - 9am to 3pm", "Thursday - 11am to 5pm"],
        "bio": "Charbel is a registered dietitian focusing on weight management and diabetes care."
    },
    "Manouella Helou, CN": {
        "specialization": "Pediatric Nutrition",
        "contact": "ManouellaHelou@nutriswap.com",
        "image": "Manouella.jpg",
        "availability": ["Wednesday - 10am to 4pm", "Friday - 1pm to 7pm"],
        "bio": "Manouella is a certified nutritionist with expertise in children's nutrition."
    }
}

# Sample data for user testimonials
user_testimonials = [
    {
        "name": "Adam Salha",
        "date": "2023-07-15",
        "image": "adam.jpg" ,
        "testimonial": (
            "Joining NutriSwap Kitchen was a game-changer for me! The personalized diet plans and "
            "consultations with the nutritionists have helped me tremendously in achieving my health goals. "
            "I've never felt better!"
        ),
    },
    {
        "name": "Houssam Chbichib",
        "date": "2023-06-10",
        "image": "Houssam.jpg" ,
        "testimonial": (
            "The educational content and healthy recipes transformed the way I think about food. "
            "I've learned so much about nutrition and healthy eating habits. Highly recommend!"
        ),
    },{
        "name": "Pipo",
        "date": "2023-08-01",
        "image": "Pipo.jpg" ,
        "testimonial": (
            "NutriSwap Kitchen has completely altered my approach to eating and wellness. The insightful "
            "advice from my nutritionist and the wealth of educational resources available have been invaluable. "
            "It's a journey worth taking for anyone serious about their health."
        ),
       
    },
    {
        "name": "Mohamad Ayoub",
        "date": "2023-07-25",
        "image": "Ayoub.jpg" ,
        "testimonial": (
            "As someone who struggled with dietary choices, the guidance I received from NutriSwap Kitchen "
            "was transformative. The recipes are not only healthy but also incredibly delicious, making healthy eating a joy."
        ),
        
    },
    {
        "name": "Fouad Zablith",
        "date": "2023-07-18",
        "image": "C:/path_to_alex_image.jpg" ,
        "testimonial": (
            "The blend of expert nutrition advice and practical, tasty recipes has made a significant impact "
            "on my lifestyle. I appreciate the personalized approach and the supportive community."
        ),
        
    },
]

# Function to sort testimonials
def sort_testimonials(testimonials, sort_order):
    return sorted(testimonials, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=sort_order == "Most Recent")


# The list of providers with their information
providers = [
    {
        "name": "Diet Box",
        "location": "Mtayleb, Lebanon",
        "phone": ["76509787", "03129456"],
        "website": "https://www.findhealthclinics.com/LB/Beirut/228075533982954/DIET-BOX#contact"
    },
    {
        "name": "Go Light",
        "location": "Rabieh, Lebanon",
        "phone": ["03050881"],
        "website": "https://www.facebook.com/Golightgourmet/"
    },
    {
        "name": "Mama's Apron",
        "location": "Beirut, Lebanon",
        "phone": ["81277667"],
        "website": ""  # Add website if available
    },
    {
        "name": "HealthBox",
        "location": "Beirut, Lebanon",
        "phone": ["05456775"],  # Add phone numbers if available
        "website": ""  # Add website if available
    },
    # Add more providers as needed
]

def display_providers(providers):
    st.subheader("Connect with Healthy Food Providers")
    for provider in providers:
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(provider["name"])
            with col2:
                st.write(provider["location"])
            with col3:
                for phone in provider["phone"]:
                    st.write(f"📞 {phone}")
            st.write(f"[Website]({provider['website']})" if provider["website"] else "Website not available")

# Main App Function
def main():
    st.title('NutriSwap Kitchen')

    st.sidebar.title("Features")
    option = st.sidebar.radio("Choose a feature", 
                              ["Home", "BMI Calculator", "Eat Healthy", "Educational Content", 
                               "Connect with a Nutritionist", "Healthy Food Provider", 
                               "User Testimonials"])


    if option == "Home":
        if option == "Home":
            image_path = "Nutriswap logo.jpg"
            if os.path.isfile(image_path):
                    st.image(image_path, use_column_width=True)
            else:
                st.error(f"Failed to find image at {image_path}")
            st.subheader("Discover a Healthier You with NutriSwap Kitchen")
            st.write(
            """
            Embark on a culinary adventure where flavor meets nutrition. NutriSwap Kitchen is your partner in redefining indulgence with a healthy twist. 
            Say goodbye to guilt and hello to pleasure, as we transform your food cravings into nourishing, delectable meal options. 
            Join us on a journey to wellness, where each bite is a step towards a balanced, vibrant life. 
            It's not just about eating differently; it's about living better. Welcome to your new food philosophy!
            """
        )


    elif option == "BMI Calculator":
        st.subheader("BMI Calculator")
        weight = st.number_input("Enter your weight (in kg):", min_value=1.0)
        height = st.number_input("Enter your height (in cm):", min_value=1.0)
        if st.button("Calculate BMI"):
            bmi, category = calculate_bmi(weight, height)
            st.write(f"Your BMI is {bmi:.2f}. Based on your BMI, you are categorized as {category}.")

    elif option == "Eat Healthy":
        st.subheader("Eat Healthy")
        st.subheader("Healthy Food Alternative Recipes")
        # Dietary preference selection
        diet_pref = st.radio("Select your dietary preference:", ('Any', 'Vegetarian', 'Vegan', 'Gluten-Free'))
        # User selects their craving
        craving = st.selectbox('Select your craving:', list(recipes.keys()))

        # Display the recipe based on dietary preference
        selected_recipe = recipes[craving]
        if diet_pref == 'Any' or any(diet_pref in tag for tag in selected_recipe['tags']):
            st.subheader("Recipe: " + craving)
            st.write("Description:", selected_recipe['description'])
            st.write("Ingredients:", ', '.join(selected_recipe['ingredients']))
            st.write("Preparation Steps:", selected_recipe['preparation'])
            st.write("Nutritional Information:", selected_recipe['nutritional_info'])
        else:
            st.write(f"Sorry, there are no {diet_pref} options available for {craving}.")
        # Implement the 'Eat Healthy' feature here

    elif option == "Educational Content":

        st.subheader("Educational Content and Tips")

        st.write("""
        ## 🍎 Daily Nutrition Facts

        **Did you know?** 
        - Eating a variety of colorful fruits and vegetables can provide a wide range of vitamins and minerals. Each color provides unique nutritional benefits!
        - Drinking water before meals can aid in weight loss, as it helps to fill your stomach, reducing the likelihood of overeating.
        - Spices like turmeric, ginger, and cinnamon not only add flavor to your meals but also contain anti-inflammatory properties.
        
        ## 🌿 Tips for a Balanced Diet
        1. **Include more plant-based foods:** Aim for at least five servings of fruits and vegetables each day.
        2. **Choose whole grains over refined grains:** Whole grains like brown rice and whole wheat bread contain more fiber and nutrients.
        3. **Limit added sugars and salt:** Be mindful of the sugar and salt content in processed foods.
        4. **Stay hydrated:** Aim to drink at least 8 glasses of water daily.
        5. **Practice mindful eating:** Pay attention to your hunger cues and eat slowly to enjoy your food.

        ## 🏋️‍♂️ Fitness Corner
        **Exercise Tip of the Day:**
        - A brisk 30-minute walk each day can significantly improve cardiovascular health and help in maintaining a healthy weight.

        ## 🥑 Healthy Recipe Idea
        **Today's Recipe: Avocado and Chickpea Salad**
        - A quick, nutritious salad packed with healthy fats, protein, and fiber. Ideal for a refreshing lunch!
        
        ## 🧘‍♀️ Wellness and Mindfulness
        - **Mindfulness Meditation:** Taking 10 minutes each day to meditate can reduce stress, improve focus, and promote a sense of calm.
        - **Gratitude Journaling:** Writing down three things you're grateful for each day can enhance positivity and overall well-being.
        """)

   
    elif option == "Connect with a Nutritionist":
        st.subheader("Connect with a Nutritionist")

        for name, details in nutritionists.items():
            with st.expander(name):
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.image(details["image"], width=100)  # Display the nutritionist's image
                with col2:
                    st.write(f"**Specialization:** {details['specialization']}")
                    st.write(f"**Contact:** {details['contact']}")
                    st.write(f"**Availability:** {', '.join(details['availability'])}")
                    st.write(f"**Bio:** {details['bio']}")

                # Unique key for each date_input widget
                unique_key = "date_" + name.replace(" ", "_").lower()
                appointment_date = st.date_input("Select a date for your appointment", 
                                                 min_value=datetime.today(), 
                                                 key=unique_key)

                if st.button(f"Book an appointment with {name.split(',')[0]}", key=f"btn_{unique_key}"):
                    st.success(f"Appointment booked with {name} on {appointment_date.strftime('%Y-%m-%d')}")
    elif option == "Healthy Food Provider":
        display_providers(providers)


    elif option == "User Testimonials":
        st.subheader("User Testimonials and Success Stories")

        # Add a banner or image at the top of the testimonials section
        st.image("C:/Users/Chekri/Desktop/Streamlit App images/Logo.png", use_column_width=True)  # Replace with the path to your image

        sort_order = st.selectbox("Sort testimonials by:", ["Most Recent", "Oldest First"])
        sorted_testimonials = sort_testimonials(user_testimonials, sort_order)

        for testimonial in sorted_testimonials:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(testimonial["image"], width=100)  # Display the user's image
            with col2:
                st.write(f"### {testimonial['name']}")
                st.write(f"_Date: {testimonial['date']}_")
                st.write(f"_{testimonial['testimonial']}_")
            st.markdown("---")

        # Call-to-action for submitting testimonials
        st.subheader("Share Your Story")
        st.write("""
            We love hearing from our users! If you have a story or experience you'd like to share about how NutriSwap Kitchen has impacted your life, 
            please reach out to us. Send your testimonials to testimonials@nutriswapkitchen.com . 
            Your journey could inspire and motivate others!
        """)


# Run the app
if __name__ == "__main__":
    main()
