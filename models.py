from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class People(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField(null=False)
    email = models.EmailField()
    password=models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField(default=0)
    
class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField( max_length=50,default="DEFAULT VALUE")
    age  = models.IntegerField(null=False)
    email = models.EmailField(null=False,unique=True)
    
    door = models.CharField(max_length=20,default="null",null=False)
    street = models.CharField(max_length=200,default="null",null=False)
    city = models.CharField(max_length=200,default="null",null=False)
    state = models.CharField(max_length=200,default="null",null=False)
    date = models.CharField(max_length=50,null=False,default="00/00/0000")
    phone = models.CharField(unique=True,max_length=100)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField( max_length=1000,default="DEFAULT VALUE")
    age  = models.IntegerField(null=False)
    email = models.EmailField(null=False,unique=True)
    

    door = models.CharField(max_length=20,default="null",null=False)
    street = models.CharField(max_length=1000,default="null",null=False)
    city = models.CharField(max_length=200,default="null",null=False)
    state = models.CharField(max_length=200,default="null",null=False)
    date = models.CharField(max_length=1000,null=False,default="00/00/0000")
    phone = models.CharField(unique=True,max_length=1000)
    
    
class Counselor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField( max_length=50,default="DEFAULT VALUE")
    age  = models.IntegerField(null=False)
    email = models.EmailField(null=False,unique=True)
    
    door = models.CharField(max_length=20,default="null",null=False)
    street = models.CharField(max_length=200,default="null",null=False)
    city = models.CharField(max_length=200,default="null",null=False)
    state = models.CharField(max_length=200,default="null",null=False)
    date = models.CharField(max_length=50,null=False,default="00/00/0000")
    phone = models.CharField(unique=True,max_length=100)
    

class common(models.Model):
    
    cmn = models.FileField( upload_to =  'uploads/' )
class Anxiety(models.Model):
    ques1 = models.FileField( upload_to =  'anxiety/' )
    ques2 = models.FileField( upload_to =  'anxiety/' )
    ques3 = models.FileField( upload_to =  'anxiety/' )
    ques4 = models.FileField( upload_to =  'anxiety/' )
    ques5 = models.FileField( upload_to =  'anxiety/' ) 
class Stress(models.Model):
    ques1 = models.FileField( upload_to =  'stress/' )
    ques2 = models.FileField( upload_to =  'stress/' )
    ques3 = models.FileField( upload_to =  'stress/' )
    ques4 = models.FileField( upload_to =  'stress/' )
    ques5 = models.FileField( upload_to =  'stress/' )
    ques6 = models.FileField( upload_to =  'stress/' )
    ques7 = models.FileField( upload_to =  'stress/' )
class Anxiety_Stag2(models.Model):
    sno = models.IntegerField()
    ques = models.CharField(max_length=100)
    op1 = models.CharField(max_length=150)
    op2 = models.CharField(max_length=150)
    op3 = models.CharField(max_length=150)
    op4 = models.CharField(max_length=150)
class Anxiety_Stag2_ans(models.Model):
    Profile = models.OneToOneField(Profile,on_delete=models.CASCADE,null=True)
    ans1 = models.CharField(max_length=100)
    ans2 = models.CharField(max_length=100)
    ans3 = models.CharField(max_length=100)
    ans4 = models.CharField(max_length=100)
    ans5 = models.CharField(max_length=100)
    ans6 = models.CharField(max_length=100)
    ans7 = models.CharField(max_length=100)
    
class Stress_Stag2(models.Model):
    
    sno = models.IntegerField()
    ques = models.CharField(max_length=100)
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)
class Stress_Stag2_ans(models.Model):
    Profile = models.OneToOneField(Profile,on_delete=models.CASCADE,null=True)
    ans1 = models.CharField(max_length=100)
    ans2 = models.CharField(max_length=100)
    ans3 = models.CharField(max_length=100)
    ans4 = models.CharField(max_length=100)
    ans5 = models.CharField(max_length=100)
    

questions=   {
"stage3":{
"panic_questions":{
    "ques1":
        {
            "question_display":"Felt moments of sudden terror, fear or fright, sometimes out of the blue (i.e., a panic attack)",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        },
        "ques2":
        {
            "question_display":"Felt anxious, worried, or nervous about having more panic attacks",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        },
        "ques3":
        {
            "question_display":"Had thoughts of losing control, dying, going crazy, or other bad things happening because of panic attacks",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        },
        "ques4":
        {
            "question_display":"Felt a racing heart, sweaty, trouble breathing, faint, or shaky",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        },
        "ques5":
        {
            "question_display":"Felt tense muscles, felt on edge or restless, or had trouble relaxing or trouble sleeping",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        },
        "ques6":
        {
            "question_display":"Avoided, or did not approach or enter, situations in which panic attacks might occur",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        },
        "ques7":
        {
            "question_display":"Left situations early, or participated only minimally, because of panic attacks",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        },
        "ques8":
        {
            "question_display":"Spent a lot of time preparing for, or procrastinating about (putting off), situations in which panic attacks might occur",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        },
        "ques9":
        {
            "question_display":"Distracted myself to avoid thinking about panic attacks",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        },
        "ques10":
        {
            "question_display":"Needed help to cope with panic attacks (e.g., alcohol or medication, superstitious objects, other people)",
            "answer_choices":{
                "0":"Never",
                "1":"Occasionally",
                "2":"Half of the time",
                "3":"Most of the time",
                "4":"All of the time"
            }
        }
    
} ,
"gad_questions" : {
    "ques1":
        {
            "question_display":"Feeling nervous, anxious, or on edge",
            "answer_choices":{
                "0":"Not at all",
                "1":"Several days",
                "2":"More than half the days",
                "3":"Nearly every day"
            }
        },
        "ques2":
        {
            "question_display":"Not being able to stop or control worrying",
            "answer_choices":{
                "0":"Not at all",
                "1":"Several days",
                "2":"More than half the days",
                "3":"Nearly every day"
            }
        },
        "ques3":
        {
            "question_display":"Worrying too much about different things",
            "answer_choices":{
                "0":"Not at all",
                "1":"Several days",
                "2":"More than half the days",
                "3":"Nearly every day"
            }
        },
        "ques4":
        {
            "question_display":"Trouble relaxing",
            "answer_choices":{
                "0":"Not at all",
                "1":"Several days",
                "2":"More than half the days",
                "3":"Nearly every day"
            }
        },
        "ques5":
        {
            "question_display":"Being so restless that it is hard to sit still",
            "answer_choices":{
                "0":"Not at all",
                "1":"Several days",
                "2":"More than half the days",
                "3":"Nearly every day"
            }
        },
        "ques6":
        {
            "question_display":"Becoming easily annoyed or irritable",
            "answer_choices":{
            "0":"Not at all",
            "1":"Several days",
            "2":"More than half the days",
            "3":"Nearly every day"
            }
        },
        "ques7":
        {
            "question_display":"Feeling afraid, as if something awful might happen",
            "answer_choices":{
            "0":"Not at all",
            "1":"Several days",
            "2":"More than half the days",
            "3":"Nearly every day"
            }
        }
}, 
"acute_questions" : {
    "ques1":
        {
            "question_display":"Having “flashbacks,” that is, you suddenly acted or felt as if a stressful experience from the past was happening all over again (for example, you reexperienced parts of a stressful experience by seeing, hearing, smelling, or physically feeling parts of the experience)?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques2":
        {
            "question_display":"Feeling very emotionally upset when something reminded you of a stressful experience?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques3":
        {
            "question_display":"Feeling detached or distant from yourself, your body,your physical surroundings, or your memories? ",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques4":
        {
            "question_display":"Trying to avoid thoughts, feelings, or physical sensations that reminded you of a stressful experience?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques5":
        {
            "question_display":"Being 'super alert,' on guard, or constantly on the lookout for danger? ",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques6":
        {
            "question_display":"Feeling jumpy or easily startled when you hear an unexpected noise",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques7":
        {
            "question_display":"Being extremely irritable or angry to the point where you yelled at other people, got into fights, or destroyed things?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        }
}, 
"ptsd_questions" : {
    "ques1":
        {
            "question_display":"Repeated, disturbing, and unwanted memories of the stressful experience?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques2":
        {
            "question_display":"Repeated, disturbing dreams of the stressful experience?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques3":
        {
            "question_display":"Suddenly feeling or acting as if the stressful experience were actually happening again (as if you were actually back there reliving it)?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques4":
        {
            "question_display":"Feeling very upset when something reminded you of the stressful experience?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques5":
        {
            "question_display":"Having strong physical reactions when something reminded you of the stressful experience (for example, heart pounding, trouble breathing, sweating)?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques6":
        {
            "question_display":"Avoiding memories, thoughts, or feelings related to the stressful experience?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques7":
        {
            "question_display":"Avoiding external reminders of the stressful experience (for example, people, places, conversations, activities, objects, or situations)?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques8":
        {
            "question_display":"Trouble remembering important parts of the stressful experience?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques9":
        {
            "question_display":"Having strong negative beliefs about yourself, other people, or the world (for example, having thoughts such as: I am bad, there is something seriously wrong with me, no one can be trusted, the world is completely dangerous)?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques10":
        {
            "question_display":"Blaming yourself or someone else for the stressful experience or what happened after it?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques11":
        {
            "question_display":"Having strong negative feelings such as fear, horror, anger, guilt, or shame?",
            "answer_choices":{
                 "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques12":
        {
            "question_display":"Loss of interest in activities that you used to enjoy?",
            "answer_choices":{
                 "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques13":
        {
            "question_display":"Feeling distant or cut off from other people?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques14":
        {
            "question_display":"Trouble experiencing positive feelings (for example, being unable to feel happiness or have loving feelings for people close to you)?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques15":
        {
            "question_display":"Irritable behavior, angry outbursts, or acting aggressively?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques16":
        {
            "question_display":"Taking too many risks or doing things that could cause you harm?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques17":
        {
            "question_display":"Being “superalert” or watchful or on guard?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques18":
        {
            "question_display":"Feeling jumpy or easily startled?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques19":
        {
            "question_display":"Having difficulty concentrating?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        },
        "ques20":
        {
            "question_display":"Trouble falling or staying asleep?",
            "answer_choices":{
                "0":"Not at all",
                "1":"A little bit",
                "2":"Moderately",
                "3":"Quite a bit",
                "4":"Extremely"
            }
        }
        
},
"sias_questions" :{
    "ques1":
        {
            "question_display":"I get nervous if I have to speak with someone in authority (teacher, boss, etc.)",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques2":
        {
            "question_display":" I have difficulty making eye contact with others",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques3":
        {
            "question_display":"I become tense if I have to talk about myself or my feelings.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques4":
        {
            "question_display":" I find it difficult to mix comfortably with the people I work with.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques5":
        {
            "question_display":"I find it easy to make friends my own age",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques6":
        {
            "question_display":"I tense up if I meet an acquaintance in the street",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques7":
        {
            "question_display":"When mixing socially, I am uncomfortable.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques8":
        {
            "question_display":"I feel tense if I am alone with just one other person",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques9":
        {
            "question_display":"I am at ease meeting people at parties, etc",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques10":
        {
            "question_display":"I have difficulty talking with other people",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques11":
        {
            "question_display":" I find it easy to think of things to talk about.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques12":
        {
            "question_display":"I worry about expressing myself in case I appear awkward.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques13":
        {
            "question_display":"I find it difficult to disagree with another’s point of view",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques14":
        {
            "question_display":"I have difficulty talking to attractive persons of the opposite sex.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques15":
        {
            "question_display":" I find myself worrying that I won’t know what to say in social situations",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques16":
        {
            "question_display":"I am nervous mixing with people I don’t know well.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques17":
        {
            "question_display":" I feel I’ll say something embarrassing when talking.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques18":
        {
            "question_display":"When mixing in a group, I find myself worrying I will be ignored.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques19":
        {
            "question_display":"I am tense mixing in a group.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        },
        "ques20":
        {
            "question_display":" I am unsure whether to greet someone I know only slightly.",
            "answer_choices":{
                "0":"Not at all",
                "1":"Slightly",
                "2":"Moderately",
                "3":"Very",
                "4":"Extremely"
            }
        }
        
},
"adjust_questions":{
    "ques1": {
    "question_display": "I worry a lot more since the stressful event(s)",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    },
    "ques2": {
    "question_display": " I can’t stop thinking about the stressful event(s).",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    },
    "ques3": {
    "question_display": ". I often feel afraid about what might happen in the future since the stressful event(s).",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    },
    "ques4": {
    "question_display": " I find it difficult to adapt to life since the stressful event(s).",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    },
    "ques5": {
    "question_display": "I find it difficult to relax and feel calm since the stressful event(s).",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    },
    "ques6": {
    "question_display": " I find it difficult to achieve a state of inner peace since the stressful event(s).",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    },
    "ques7": {
    "question_display": ". Did these problems start within one month of the stressful event(s)?",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    },
    "ques8": {
    "question_display": "Affected your relationships or social life?",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    },
    "ques9": {
    "question_display": "Affected your ability to work or your educational life?",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    },
    "ques10": {
    "question_display": "Affected any other important part of your life?",
    "answer_choices": {
        "0": "Not at all",
        "1": "A little Bit",
        "2": "Moderately",
        "3": "Quite a Bit",
        "4": "Extremely"
    }
    }
}
},
"stage2":{
"anxiety_questions":{
    "ques1": {
    "question_display": "Where often you experience the anxiety?",
    "answer_choices": {
        "0": "Generally everywhere in all everyday activities",
        "1": "Mainly in social gatherings",
        "2": "Particular threat like any place or some things",
        "3": "others"
    }
    },
    "ques2": {
    "question_display": " How do you feel when you are anxious?",
    "answer_choices": {
        "0": "All the below",
        "1": "Increased heart rate,fatigue,tremble",
        "2": "Irritability,chest pain,feel losing over control",
        "3": "You feel nervous and sweat all time"
    }
    },
    "ques3": {
    "question_display": "How long you are worrying or feeling anxious?",
    "answer_choices": {
        "0": "1-2 months",
        "1": "4-6 months",
        "2": "Less than a week",
        "3": "More than 6 months"
    }
    },
    "ques4": {
    "question_display": "Do you have any of these?",
    "answer_choices": {
        "0": "Difficulty functioning everyday activities",
        "1": "Do you get chills and tingling when anxious",
        "2": "Lack of interaction to avoid social situations",
        "3": "Sleep disturbance or less sleep"
    }
    },
    "ques5": {
    "question_display": "Are you a person?",
    "answer_choices": {
        "0": "All the below",
        "1": "Who enjoys company of talking and being with other people",
        "2": "Who is afraid of talking,drawing attention to yourself and risking anticipated embarrassment",
        "3": "Who worry about everyday life events for no obvious reason"
    }
    },
    "ques6": {
    "question_display": "Do you feel any of these in your day to day life?",
    "answer_choices": {
        "0": "All the below",
        "1": "Exaggerated worry and tension,even when there is little or nothing to provoke it",
        "2": "Excessive self-consciousness in everyday social situations",
        "3": "Repeated episodes of intense fear"
    }
    },
    "ques7": {
    "question_display": "What exactly makes you feel worried?",
    "answer_choices": {
        "0": "All the below",
        "1": "Day-to-day functions such as finances or life issues",
        "2": "Meeting people or surrounding yourselves in a social environment.",
        "3": "Worry about fear or terror that reach a peak within minutes."
    }
    }
},
"stress_questions":{
    "ques1": {
    "question_display": "Exposed to any threatening event like:",
    "answer_choices": {
        "0": "Accident",
        "1": "Death",
        "2": "Natural Disaster",
        "3": "other"
    }
    },
    "ques2": {
    "question_display": "When do you feel more stressed?",
    "answer_choices": {
        "0": "Others",
        "1": "When in trauma witnessed place",
        "2": "When moved to new place recently",
        "3": "When you see specific stimuli"
    }
    },
    "ques3": {
    "question_display": "Time  experiencing the stress",
    "answer_choices": {
        "0": "2-3 months",
        "1": "5-6 months",
        "2": "A week or less",
        "3": "More than 6 months"
    }
    },
    "ques4": {
    "question_display": "Do you have any of these behaviours? ",
    "answer_choices": {
        "0": "Feel that change of place is real stress",
        "1": "Hyper Vigilance",
        "2": "Recurrent dreams",
        "3": "Startled responses"
    }
    },
    "ques5": {
    "question_display": "Do you feel any of these below?",
    "answer_choices": {
        "0": "Avoidance",
        "1": "Avoiding going to place where some life threat happened",
        "2": "Loss of job/divorce/breakup or any other  recently",
        "3": "No sleep for 48 hours"
    }
    }
    }
    }
}






    



class Stage0(models.Model):
    Profile = models.OneToOneField(Profile,on_delete=models.CASCADE,null=True)
    Greetings = models.CharField(max_length=100)
    Wellbeing = models.CharField(max_length=500)
    About = models.CharField(max_length=500)
    Strengths = models.CharField(max_length=500)
    Reason = models.CharField(max_length=500)
    Therapy = models.CharField(max_length=500)
    Magical_Wish = models.CharField(max_length=500)
    Favourite_Food = models.CharField(max_length=500)
    Friend_Characteristics = models.CharField(max_length=500)
    Last_Angry = models.CharField(max_length=500)
    Not_like_to_do_at_home = models.CharField(max_length=500)
class Stage1(models.Model):
    Profile = models.OneToOneField(Profile,on_delete=models.CASCADE,null=True)
    greetings = models.CharField(max_length=100)
    readiness = models.CharField(max_length=100)
    ques1 = models.CharField(max_length=4)
    ques2 = models.CharField(max_length=4)
    ques3 = models.CharField(max_length=4)
    ques4 = models.CharField(max_length=4)
    ques5 = models.CharField(max_length=4)
    ques6 = models.CharField(max_length=4)
    ques7 = models.CharField(max_length=4)
    ques8 = models.CharField(max_length=4)
    ques9 = models.CharField(max_length=4)
    ques10 = models.CharField(max_length=4)
    ques11 = models.CharField(max_length=4)
    ques12 = models.CharField(max_length=4)
    ques13 = models.CharField(max_length=4)
    ques14 = models.CharField(max_length=4)
    ques15 = models.CharField(max_length=4)
    ques16 = models.CharField(max_length=4)
    ques17 = models.CharField(max_length=4)
    ques18 = models.CharField(max_length=4)
    ques19 = models.CharField(max_length=4)
    ques20 = models.CharField(max_length=4)
    ques21 = models.CharField(max_length=4)
    ques22 = models.CharField(max_length=4)
    stress = models.CharField(max_length=4)
    anxiety = models.CharField(max_length=4)
    


class Stageone(models.Model):
    Profile = models.OneToOneField(Profile,on_delete=models.CASCADE,null=True)
    greetings = models.CharField(max_length=100)
    readiness = models.CharField(max_length=100)
    ques1 = models.CharField(max_length=4)
    ques2 = models.CharField(max_length=4)
    ques3 = models.CharField(max_length=4)
    ques4 = models.CharField(max_length=4)
    ques5 = models.CharField(max_length=4)
    ques6 = models.CharField(max_length=4)
    ques7 = models.CharField(max_length=4)
    ques8 = models.CharField(max_length=4)
    ques9 = models.CharField(max_length=4)
    ques10 = models.CharField(max_length=4)
    ques11 = models.CharField(max_length=4)
    ques12 = models.CharField(max_length=4)
    ques13 = models.CharField(max_length=4)
    ques14 = models.CharField(max_length=4)
    
    stress = models.CharField(max_length=4)
    anxiety = models.CharField(max_length=4)
    


class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)
    select = models.CharField(max_length=100,null=False,default="disorder")
    def __str__(self):
        return self.name
class Result(models.Model):
    Profile = models.OneToOneField(Profile,on_delete=models.CASCADE,null=True)
    
    stage0 = models.CharField(max_length=5000,null=True,default="null")
    stage1 = models.CharField(max_length=5000,null=True,default="null")
    stage2 = models.CharField(max_length=5000,null=True,default="null")
    stage3 = models.CharField(max_length=5000,null=True,default="null")
    risk = models.CharField(max_length=100,default="null")
class Outcome(models.Model):
    Profile = models.OneToOneField(Profile,on_delete=models.CASCADE,null=True)
    
    stage0 = models.CharField(max_length=5000,null=True,default="null")
    stage1 = models.CharField(max_length=5000,null=True,default="null")
    stage2 = models.CharField(max_length=5000,null=True,default="null")
    stage3 = models.CharField(max_length=5000,null=True,default="null")
    risk = models.CharField(max_length=100,default="null")
class Appoint(models.Model):
    Profile = models.OneToOneField(Profile,on_delete=models.CASCADE) 
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    date = models.CharField(max_length=100,default="null",unique=False)
    time = models.CharField(max_length=100,default="null",unique=False)

class Past_Appoint(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    date = models.CharField(max_length=100,default="null",unique=False)
    time = models.CharField(max_length=100,default="null",unique=False)
    session = models.CharField(max_length=100,default="1",unique=False)

class Treatment(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    session = models.CharField(max_length=100,unique=False)
    treat = models.CharField(max_length=1000)
class Answers(models.Model):
    ans_id = models.CharField(max_length=100,null=True)
    ques_id =models.CharField(max_length=100,null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)  
    ques_category = models.CharField(max_length=100,null=True)
    stage =models.CharField(max_length=100,null=True)
class Severity(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)
    res = models.CharField(max_length=4)
