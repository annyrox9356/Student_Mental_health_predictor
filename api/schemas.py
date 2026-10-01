from pydantic import BaseModel,Field,field_validator
from typing import Annotated,Literal

class Data_validator(BaseModel):
    Age:Annotated[int,Field(gt=0,lt=120,description="enter your age" ,examples=[18,34])]
    Gender:Annotated[Literal['Male','Female'],Field(description="choose either Male or Female",examples=['Male','Female'])]
    Country:Annotated[str,Field(description="enter the country you live in",examples=['India','USA','Morocco'])]
    Academic_Level:Annotated[str,Field(description="Enter your education level",examples=["Undergraduate"])]
    Most_Used_Platform:Annotated[str,Field(description="which plateform do you use most",examples=['Facebook','Instagram','LinkedIn'])]
    Purpose_Of_Use:Annotated[Literal['Networking','Education','Entertainment','News'],Field(description="enter the purpose of use of the plateform",examples=['Entertainment','News'])]
    Avg_Daily_Usage_Hours:Annotated[float,Field(gt=0,description="enter no. of hours you daily uses of smartphone",examples=[12.3,2.3,4,7])]
    Daily_Unlocks:Annotated[int,Field(gt=0,description="How many times you unlocks your phone",examples=[12,35,76,124])]
    Study_Hours:Annotated[float,Field(gt=0,description="no. of hours you study",examples=[12.4,3.4,6])]
    Physical_Activity_Hours:Annotated[float,Field(gt=0,description="no. of hours you do physical activity",examples=[2.2,3,0.7])]
    Sleep_Hours_Per_Night:Annotated[float,Field(gt=0,description="no. og hours you sleep daily",examples=[6.7,8.6,6.7,5.4,5])]
    Stress_Level:Annotated[str,Field(description="according to you, your stress level",examples=['Medium','Low','Very High','High'])]



    @field_validator("Gender","Purpose_Of_Use",mode='before')
    @classmethod
    def convert_to_title_case(cls, value):
        return value.title()

    @field_validator("Country", mode='before')
    @classmethod
    def format_country(cls, value):
        if isinstance(value, str):
            clean_val = value.strip().upper()
            # Preserve abbreviations used in your JSON mapping
            if clean_val in ['USA', 'UK', 'UAE']:
                return clean_val
            return value.strip().title()
        return value
    
    @field_validator('Most_Used_Platform')
    @classmethod
    def format_platform(cls, value: str) -> str:
        # User ne jo bhi dala usko lowercase kar lo aur spaces hata do
        clean_value = value.strip().lower()
        
        # CSV ke exact casing ke hisaab se mapping
        platform_mapping = {
            "facebook": "Facebook",
            "linkedin": "LinkedIn",
            "instagram": "Instagram",
            "snapchat": "Snapchat",
            "twitter": "Twitter",
            "youtube": "YouTube",
            "tiktok": "TikTok",
            "line": "LINE",
            "kakaotalk": "KakaoTalk",
            "vkontakte": "VKontakte",
            "whatsapp": "WhatsApp",
            "wechat": "WeChat"
        }
        
        # Agar platform list me hai, toh exact CSV format return karo
        if clean_value in platform_mapping:
            return platform_mapping[clean_value]
            
        # Agar user koi anjaan platform daale toh error raise karo
        raise ValueError(f"Platform must be one of: {list(platform_mapping.values())}")

    @field_validator('Stress_Level')
    @classmethod
    def format_stress_level(cls, value: str) -> str:
        # User input se saare spaces hata kar lowercase me badal dein
        # Example: "Very  High" -> "veryhigh", "Low " -> "low"
        clean_value = value.strip().lower().replace(" ", "")
        
        # Mapping dictionary jo cleaned input ko CSV format se map karegi
        mapping = {
            "low": "Low",
            "medium": "Medium",
            "high": "High",
            "veryhigh": "Very High"  # Yahan hum wapas exact CSV format de rahe hain
        }
        
        if clean_value in mapping:
            return mapping[clean_value]
            
        raise ValueError(f"Stress level must be one of: {list(mapping.values())}")


    @field_validator('Academic_Level')
    @classmethod
    def format_academic_level(cls, value: str) -> str:
        # User input se saare spaces hata kar lowercase me badal dein
        # Example: "Very  High" -> "veryhigh", "Low " -> "low"
        clean_value = value.strip().lower().replace(" ", "")
            
        # Mapping dictionary jo cleaned input ko CSV format se map karegi
        mapping_Academic_Level={
            'undergraduate':'Undergraduate',
            'graduate':'Graduate',
            'highschool':'High School'
        }
        if clean_value in mapping_Academic_Level:
            return mapping_Academic_Level[clean_value]
                
        raise ValueError(f"Acedemic Level must be one of: {list(mapping_Academic_Level.values())}")

