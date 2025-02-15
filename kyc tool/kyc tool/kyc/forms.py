from django import forms
from .models import Questions

class QuestionsForm(forms.ModelForm):

    q1 = forms.ChoiceField(choices=[
    ('drama', 'Drama / Arts class'),
    ('english', 'English class'),
    ('sports', 'Sports / Physical Education'),
    ('science', 'Science / Math lab'),
    ], 
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), 
    label="1. Pick one class you like the most")

    q2 = forms.ChoiceField(choices=[
        ('draw', 'I will draw on it'),
        ('write', 'I will write on it'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="2. If you get a new notebook, what will you do with it?")

    q3 = forms.ChoiceField(choices=[
        ('read', 'Read a book / write short stories'),
        ('art', 'do art and crafts'),
        ('games', 'play video games / solve puzzles'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="3. During your free time")

    q4 = forms.ChoiceField(choices=[
        ('important_first', 'You will share the most important piece of news first and then give the details'),
        ('hand_movements', 'You will use a lot of hand movements and facial expressions while narrating'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="4. You have a good news and you want to share it with the family. While telling them,")

    q5 = forms.ChoiceField(choices=[
        ('words', 'Scrabble, Boggle (play with words)'),
        ('board', 'Monopoly / Chess'),
        ('outdoor', 'Outdoor games like football, volleyball, running etc.'),
    ], 
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="5. Pick one game you like the most")

    q6 = forms.ChoiceField(choices=[
        ('debate_book', 'Debate club / Book club'),
        ('sports', 'Sports club'),
        ('arts_drama', 'Arts / Drama club'),
    ], 
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="6. Pick one club you like the most")

    q7 = forms.ChoiceField(choices=[
        ('story_writing', 'Story writing'),
        ('laptop_activity', 'Laptop activity like coding / Puzzles'),
        ('treasure_hunt', 'Treasure hunt, Camping'),
        ('creative_activities', 'Creative activities like craft, Lego design, puzzles'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="7. Pick one activity you like the most")

    q8 = forms.ChoiceField(choices=[
        ('read_features', 'You read the product features and watch videos of the product'),
        ('compare_products', 'You see similar products and decide which one to buy'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="8. When you want to buy something new")


    q9 = forms.ChoiceField(choices=[
    ('start_reading', 'You will start reading the first chapter'),
    ('pick_interesting_topic', 'You will read the table of contents and pick out the most interesting topic'),
    ('feel_pages', 'You will touch and feel the freshness of pages'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="9. You just got a brand-new book from Amazon. The minute you have the book in your hand,")

    q10 = forms.ChoiceField(choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="10. I enjoy singing")

    q11 = forms.ChoiceField(choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="11. I like playing musical instruments")

    q12 = forms.ChoiceField(choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="12. I remember songs very easily")

    q13 = forms.ChoiceField(choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="13. I like music more than games")

    q14 = forms.ChoiceField(choices=[
        ('on_my_own', 'On my own'),
        ('with_others', 'With others'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="14. I usually play")

    q15 = forms.ChoiceField(choices=[
        ('on_my_own', 'Doing an activity on my own'),
        ('with_group', 'Doing an activity with a group'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="15. In my free time, I prefer")

    q16 = forms.ChoiceField(choices=[
        ('sit_in_room', 'I usually sit in my room and do something'),
        ('go_out', 'I like to go out and meet my friends'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="16. When I am bored")

    q17 = forms.ChoiceField(choices=[
        ('few_friends', 'Have very few friends'),
        ('many_friends', 'Have many friends'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="17. Pick one statement that represents you")

    q18 = forms.ChoiceField(choices=[
        ('sitting_alone', 'Sitting by myself in my room'),
        ('hanging_out', 'Hanging out with friends'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="18. Pick one statement that represents you")

    q19 = forms.ChoiceField(choices=[
        ('few_months', 'For a few months'),
        ('few_years', 'For a few years'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="19. How long I know my friends?")

    q20 = forms.ChoiceField(choices=[
        ('not_help', 'I usually don’t help because I’m not sure what to do'),
        ('rush_help', 'I immediately rush to help'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="20. When I see my friend hurt")

    q21 = forms.ChoiceField(choices=[
        ('hard_time', 'I have a hard time making friends'),
        ('easy_time', 'I can make friends easily'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="21. Pick one statement that represents you")

    q22 = forms.ChoiceField(choices=[
        ('not_interested', 'Not interested in meeting new people'),
        ('interested', 'Always excited to meet new people'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="22. Pick one statement that represents you")

    q23 = forms.ChoiceField(choices=[
        ('work_alone', 'I prefer to work alone'),
        ('work_group', 'I am comfortable working in a group'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="23. For school assignments")

    q24 = forms.ChoiceField(choices=[
        ('alone_room', 'I don’t spend a lot of time, I like being by myself in my room'),
        ('with_family', 'I love spending time with my family'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="24. With my family")

    q25 = forms.ChoiceField(choices=[
        ('have_or_would_like_pet', 'Have a pet/ would like to have a pet'),
        ('like_animals', 'Like animals'),
        ('scared_or_dont_like_animals', 'Scared / don’t like animals'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="25. Pick one statement that represents you")

    q26 = forms.ChoiceField(choices=[
        ('have_garden', 'I already have a small garden'),
        ('visit_garden', 'I like to visit garden'),
        ('not_interested_garden', 'I am not interested in garden'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="26. Pick one statement that represents you")

    q27 = forms.ChoiceField(choices=[
        ('beaches_zoo_garden', 'I go to beaches/zoo/garden'),
        ('mountains_beaches', 'I like mountains and beaches, but don\'t visit often'),
        ('cities_malls', 'I prefer cities/malls to beaches/mountains'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="27. Pick one statement that represents you")

    q28 = forms.ChoiceField(choices=[
        ('spot_hear_birds', 'I like to spot different birds in the sky/hear chirping sounds'),
        ('like_birds', 'I like birds but I don’t try to spot them in the sky'),
        ('dont_like_birds', 'I don’t like the sound of birds'),
    ],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="28. Pick one statement that represents you")


    class Meta:
        model = Questions
        fields = '__all__'
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'age': 'Age',
            'parentsfirstname': "Parent's First Name",
            'parentslastname': "Parent's Last Name",
            'city': 'City',
            'country': 'Country',
            'phone': 'Phone',
            'email': 'Email',
        }
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'parentsfirstname': forms.TextInput(attrs={'class': 'form-control'}),
            'parentslastname': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
