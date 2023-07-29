import streamlit as st
import numpy as np
import pandas as pd
from Image_find import new_img

df=pd.read_csv("Modified.csv")

def get_place_from_index(index):
	return df[df.index == index]["Place"].values[0]

def get_index_from_city(city):
	return df[df.City == city]["index"].values[0]

def get_index_from_place(place):
	return df[df.Place == place]["index"].values[0]

def get_city_from_index(index):
	return df[df.index == index]["City"].values[0]

def load_matrix():
    data = np.load('similarity_matrix.npy')
    return data

similarity=load_matrix()

def show_predictions_page():
    
    st.write("""### Select the city you want to visit ###""")

    cities = (
        "New Delhi",
        "Mumbai",
        "Bengaluru",
        "Hyderabad",
        "Agra",
        "Jaipur",
        "Udaipur",
        "Kolkata",
        "Agartala",
        "Chennai",
        # "Pune",
        # "Mysuru (Mysore)",
        # "Amer",
        # "Kochi (Cochin)",
        # "Ahmedabad",
        # "Srinagar",
        # "Ooty",
        # "Gangtok",
        # "Leh",
        # "Amritsar",
        # "Jodhpur",
        # "Varanasi",
        # "Manali",
        # "Shimla",
        # "Darjeeling",
        # "Jaisalmer",
        # "Pondicherry",
        # "Munnar",
        # "Gurugram (Gurgaon)",
        # "Trivandrum",
        # "Kodaikanal",
        # "South Andaman Island",
        # "Chandigarh",
        # "Visakhapatnam (Vizag)",
        # "Khopoli",
        # "Lonavala",
        # "Mussoorie",
        # "Puri",
        # "Nainital",
        # "Kalpetta",
        # "Mahabaleshwar",
        # "Mahabalipuram",
        # "Panjim",
        # "Havelock Island",
        # "Hampi",
        # "Kanyakumari",
        # "Mount Abu",
        # "Lucknow",
        # "McLeod Ganj",
        # "Rishikesh",
        # "Nashik",
        # "Baga",
        # "Madurai",
        # "Rameswaram",
        # "Aurangabad",
        # "Bhubaneswar",
        # "Thekkady",
        # "Tirupati",
        # "Haridwar",
        # "Vadodara",
        # "Coimbatore",
        # "Shillong",
        # "Indore",
        # "Sawai Madhopur",
        # "Madikeri",
        # "Bhopal",
        # "Guwahati",
        # "Noida",
        # "Dharamsala",
        # "Pushkar",
        # "Mangalore",
        # "Alappuzha",
        # "Shirdi",
        # "Chikmagalur",
        # "Navi Mumbai",
        # "Gulmarg",
        # "Yercaud",
        # "Kovalam",
        # "Pahalgam",
        # "Surat",
        # "Ujjain",
        # "Dwarka",
        # "Bardez",
        # "Sohra",
        # "Bhuj",
        # "Varkala Town",
        # "Goa Velha",
        # "Calangute",
        # "Canacona",
        # "Diu",
        # "Khajuraho",
        # "Jammu City",
        # "Coonoor",
        # "Dalhousie",
        # "Vrindavan",
        # "Pelling",
        # "Ajmer",
        # "Alwar",
        # "Tiruchirappalli",
        # "Patna",
        # "Nagpur",
        # "Kolhapur",
        # "Thrissur",
        # "Gwalior",
        # "Somnath",
        # "Thanjavur",
        # "Lansdowne",
        # "Gokarna",
        # "Daman",
        # "Sadri",
        # "Bikaner",
        # "Kannur",
        # "Jabalpur",
        # "Pachmarhi",
        # "Fatehpur Sikri",
        # "Agonda",
        # "Matheran",
        # "Arpora",
        # "Allahabad",
        # "Bodh Gaya",
        # "Sinquerim",
        # "Kozhikode",
        # "Khandala",
        # "Shimoga",
        # "Panchgani",
        # "Morjim",
        # "Bharatpur",
        # "Ajanta",
        # "Thane",
        # "Junagadh",
        # "Cavelossim",
        # "Colva",
        # "Chittaurgarh",
        # "Alibaug",
        # "Kumbhalgarh",
        # "Udupi",
        # "Belur",
        # "Orchha",
        # "Ganpatipule",
        # "Neil Island",
        # "Mathura",
        # "Kasauli",
        # "Benaulim",
        # "Vypin Island",
        # "Kalimpong",
        # "Varca",
        # "Jim Corbett National Park",
        # "Vijayawada",
        # "Tawang",
        # "Kumbakonam",
        # "Saputara",
        # "Rajkot",
        # "Raipur",
        # "Ranchi",
        # "Mapusa",
        # "Chamba",
        # "Ernakulam",
        # "Dehradun",
        # "Auroville",
        # "Trimbak",
        # "Vellore",
        # "Aluva",
        # "Lachung",
        # "Kullu",
        # "Malvan",
        # "Ratnagiri",
        # "Kanchipuram",
        # "Kumarakom",
        # "Ponda",
        # "Mararikulam",
        # "Silvassa",
        # "Mandu",
        # "Chikkaballapur",
        # "Bundi",
        # "Jamnagar",
        # "Arambol",
        # "Kutch",
        # "Vythiri",
        # "Kollam",
        # "Kausani",
        # "Mollem National Park",
        # "Badami",
        # "Gandhinagar",
        # "Almora",
        # "Chail",
        # "Jamshedpur",
        # "Mukteshwar",
        # "Kottayam",
        # "Bijapur",
        # "Palakkad",
        # "Kanpur",
        # "Digha",
        # "Kurnool",
        # "Imphal",
        # "Satara",
        # "Naggar",
        # "Athirappilly",
        # "Kanoi",
        # "Dona Paula",
        # "Anjuna",
        # "Jalandhar",
        # "Bandipur",
        # "Guruvayur",
        # "Salem",
        # "Kasaragod",
        # "Chapora",
        # "Tirunelveli",
        # "Bhimtal",
        # "Murshidabad",
        # "Badrinath",
        # "Karwar",
        # "Srirangapatna",
        # "Ghaziabad",
        # "Ranikhet",
        # "Panchkula",
        # "Mandrem",
        # "Magadi",
        # "Hassan",
        # "Abhaneri",
        # "Agartala",
        # "Kangra",
        # "Kota",
        # "Valparai",
        # "Mandarmani",
        # "Mawlynnong",
        # "Nathdwara",
        # "Bhimashankar",
        # "Warangal",
        # "Palampur",
        # "Siliguri",
        # "Halebid",
        # "Dapoli",
        # "Porbandar",
        # "Kumily",
        # "Yelagiri",
        # "Murdeshwar",
        # "Sangla",
        # "Kashid",
        # "Srisailam",
        # "Velankanni",
        # "Old Goa",
        # "Mandya",
        # "Hubli-Dharwad",
        # "Howrah",
        # "Vagamon",
        # "Thiruvannamalai",
        # "Raigad",
        # "Bhavnagar",
        # "Chamoli",
        # "Belakavadi",
        # "Patnitop",
        # "Malsi",
        # "Deoghar",
        # "Chidambaram",
        # "Lepakshi",
        # "Dhanaulti",
        # "Ludhiana",
        # "Utorda",
        # "Dandeli",
        # "Kaza",
        # "Patiala",
        # "Santiniketan",
        # "Kargil",
        # "Ahmednagar",
        # "Mandi",
        # "Kottagudi",
        # "Midnapore",
        # "Kurukshetra",
        # "Margao",
        # "Palani",
        # "Namchi",
        # "Mandvi",
        # "Faridabad",
        # "Thuckalay",
        # "Kohima",
        # "Hospet",
        # "Bhagamandala",
        # "Mandla",
        # "Vasco da Gama",
        # "Diveagar",
        # "Majorda",
        # "Greater Noida",
        # "Bandhavgarh National Park",
        # "Bharuch",
        # "Malpe",
        # "Kollur",
        # "Daulatabad",
        # "Dabolim",
        # "Dharmapuri",
        # "Cansaulim",
        # "Ranthambore National Park",
        # "Kaushambi",
        # "Maheshwar",
        # "Candolim",
        # "Tiruvannamalai",
        # "Bekal",
        # "Sonamarg",
        # "Narkanda",
        # "Rajgir",
        # "Konark",
        # "Muttukadu",
        # "Omkareshwar",
        # "Subramanya",
        # "Rajahmundry",
        # "Ramnagar",
        # "Solapur",
        # "Shrivardhan",
        # "Sasan Gir",
        # "Bidar",
        # "Cuttack",
        # "Kolar",
        # "Munsiyari",
        # "Dabguli",
        # "Katra",
        # "Chitradurga",
        # "Durgapur",
        # "Ambaji",
        # "Manipal",
        # "Kas",
        # "Shingnapur",
        # "Chittoor",
        # "Kedarnath",
        # "Jhansi",
        # "Balasore",
        # "Deshnoke",
        # "Valsad",
        # "Amarkantak",
        # "Sanchi",
        # "Gaya",
        # "Naukuchiatal",
        # "Murud",
        # "Sambalpur",
        # "Kakkabe",
        # "Srikalahasti",
        # "Meerut",
        # "Belgaum",
        # "Bilaspur",
        # "Igatpuri",
        # "Dindigul",
        # "Gorakhpur",
        # "Dawki",
        # "Jalpaiguri",
        # "Mohali",
        # "Sunkadahalli",
        # "Modhera",
        # "Sakleshpur",
        # "Pattadakal",
        # "Kotagiri",
        # "Sirsi",
        # "Pothamedu",
        # "Bishnupur",
        # "Dhanbad",
        # "Malappuram",
        # "Theni",
        # "Geyzing",
        # "Rourkela",
        # "Pathanamthitta",
        # "Puttaparthi",
        # "Taoru",
        # "Jagdalpur",
        # "Hooghly",
        # "Ayodhya",
        # "Betalbatim",
        # "Tumkur",
        # "Bathinda",
        # "Secunderabad",
        # "Sringeri",
        # "Dharmasthala",
        # "Ravangla",
        # "Solan",
        # "New Tehri",
        # "Narmada",
        # "Manikaran",
        # "Pandharpur",
        # "Kannan Devan Hills",
        # "Jwalamukhi",
        # "Nellore",
        # "Tapovan",
        # "Lavasa",
        # "Chhatarpur",
        # "Virar",
        # "Nagapattinam",
        # "Chitrakoot",
        # "Sikar",
        # "Hunsur",
        # "Naldehra",
        # "Aizawl",
        # "Ukhimath",
        # "Uttarkashi",
        # "Purulia",
        # "Baratang Island",
        # "Nalanda",
        # "Anantnag",
        # "Anand",
        # "Pinjore",
        # "Bellary",
        # "Tezpur",
        # "Nanded",
        # "Gandikota",
        # "Lamayuru",
        # "Sanguem",
        # "Kaziranga National Park",
        # "Salasar",
        # "Anjarle",
        # "Kalyan",
        # "Gangotri",
        # "Rudra Prayag",
        # "Ganjam",
        # "Gondia",
        # "Karaikudi",
        # "Taradevi",
        # "Kamshet",
        # "Mirzapur",
        # "Rupnagar",
        # "Chalakudy",
        # "Anachal",
        # "Asansol",
        # "Sangli",
        # "Adilabad",
        # "Kakinada",
        # "Bogmalo",
        # "Amravati",
        # "Nahan",
        # "Champaner",
        # "Palolem",
        # "Mehsana",
        # "Joshimath",
        # "Hemis",
        # "Singalila National Park",
        # "Courtallam",
        # "Channapatna",
        # "Namakkal",
        # "Jowai",
        # "Araku Valley",
        # "Ramgarh",
        # "Bankura",
        # "Junnar",
        # "Kolad",
        # "Deeg",
        # "Pimpri-Chinchwad",
        # "Sattal",
        # "Pavagadh",
        # "Mormugao",
        # "Talacauvery",
        # "Thirunageswaram",
        # "Thenmala",
        # "Thiruchendur",
        # "Panvel",
        # "Agumbe",
        # "Bomdila",
        # "Yuksom",
        # "Karkala",
        # "Channarayapatna",
        # "Ambala",
        # "Nagarhole National Park",
        # "Gulbarga",
        # "Bakkhali",
        # "Erode",
        # "Jorhat",
        # "Nawalgarh",
        # "North Andaman Island",
        # "Baramati",
        # "Porvorim",
        # "Brahmapur",
        # "Kundapur",
        # "Tarapith",
        # "Nuvem",
        # "Tarkarli",
        # "Pollachi Town",
        # "Gajner",
        # "Panipat",
        # "Malda",
        # "Sirohi",
        # "Kushinagar",
        # "Mirik",
        # "Bambolim",
        # "Guhagar",
        # "Ranakpur",
        # "Sarahan",
        # "Bareilly",
        # "Kaladhungi",
        # "Panshet",
        # "Nileshwar",
        # "Karnal",
        # "Sariska",
        # "Guntur",
        # "Palitana",
        # "Cooch Behar",
        # "Jalgaon",
        # "Yana",
        # "Vasai",
        # "Chamarajanagar",
        # "Ashvem Beach",
        # "Kalady",
        # "Gudalur",
        # "Keylong",
        # "Nalgonda",
        # "Thottada",
        # "Cuddalore",
        # "Kanakapura",
        # "Nagercoil",
        # "Saligao",
        # "Dahanu",
        # "Itanagar",
        # "Gorumara National Park",
        # "Lonar",
        # "Yamunotri",
        # "Barmer",
        # "Loutolim",
        # "Karauli",
        # "Rohtak",
        # "Durg",
        # "Pali",
        # "Somvarpet",
        # "Kodanad",
        # "Bhilai",
        # "Bhadrachalam",
        # "Dabaspete",
        # "Covelong",
        # "Vagator",
        # "Kheda",
        # "Aritar",
        # "Shivpuri",
        # "Tiruchendur",
        # "Kurseong",
        # "Pudukkottai",
        # "Sonipat",
        # "Bordi",
        # "Vikarabad",
        # "Tiruppur",
        # "Mantralayam",
        # "Tinsukia",
        # "Jhunjhunu",
        # "Hosur",
        # "Bokaro Steel City",
        # "Bolpur",
        # "Aligarh",
        # "Nadia",
        # "Osian",
        # "Haldwani",
        # "Sulthan Bathery",
        # "Chakrata",
        # "Vengurla",
        # "Thiruvalla",
        # "Vidisha",
        # "Bhojpur",
        # "Dausa",
        # "Anaviratty",
        # "Baijnath",
        # "Devprayag",
        # "Kufri",
        # "Datia",
        # "Tharangambadi",
        # "Someshwar",
        # "Thattekad",
        # "Srivilliputhur",
        # "Una",
        # "Sagar Island",
        # "Hunder",
        # "Auli",
        # "Giridih",
        # "Navsari",
        # "Majuli",
        # "Bapatla",
        # "Thamarassery",
        # "Sundarbans National Park",
        # "Karnala",
        # "North Paravur",
        # "Kushalnagar",
        # "Sibsagar",
        # "Zirakpur",
        # "Kanger Valley National Park",
        # "Karaikal",
        # "Yellapur",
        # "Kothamangalam",
        # "Nalsarovar",
        # "Hazira",
        # "Faizabad",
        # "Peermade",
        # "Kammasandra",
        # "Karjat Town",
        # "Thalassery",
        # "Mukutmanipur",
        # "Chanderi",
        # "Anantapur",
        # "Nagaur",
        # "Jaunpur",
        # "Alchi",
        # "Chiplun",
        # "Thiruvarur",
        # "Nagarjuna Sagar",
        # "Kodungallur",
        # "Devikulam",
        # "Gangolihat",
        # "Mayapur",
        # "Binsar",
        # "Hogenakkal",
        # "Chundale",
        # "Pathankot",
        # "Palghar",
        # "Thariyode",
        # "Dimapur",
        # "Ramanagara",
        # "Diskit",
        # "Temi",
        # "Annavaram",
        # "Shegaon",
        # "Nelliyampathy",
        # "Talakad",
        # "Tenkasi",
        # "Poicha",
        # "Chandrapur",
        # "Keonjhar",
        # "Ratlam",
        # "Tuljapur",
        # "Buldana",
        # "Parli Vaijnath",
        # "Panna",
        # "Chandor",
        # "Nilambur",
        # "Bhandardara",
        # "Wardha",
        # "Vajreshwari",
        # "Muzaffarpur",
        # "Salangpur",
        # "Nadiad",
        # "Zuluk",
        # "Bhilwara",
        # "Vizianagaram",
        # "Medak",
        # "Bhagalpur",
        # "Rewa",
        # "Burhanpur",
        # "Banswara",
        # "Chandannagar",
        # "Bangaram",
        # "Khurda",
        # "Kalol",
        # "Surendranagar",
        # "Hazaribagh",
        )

    city = st.selectbox("City",cities)

    ok = st.button("See Results")

    if(ok):
        st.write("""### Matches related to your search query ###""")
        index = get_index_from_city(city)
        similar = list(enumerate(similarity[index]))
        sort_sim = sorted(similar,key=lambda x:x[1],reverse=True)
        i=0
        for destination in sort_sim:
            place=get_place_from_index(destination[0])
            citi=get_city_from_index(destination[0])
            st.subheader(f"${place},                                    ${citi}")
            new_img(place)
            i=i+1
            if(i>20):
               break
