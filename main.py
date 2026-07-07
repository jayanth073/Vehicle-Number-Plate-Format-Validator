def state(number):

  number=number.upper()

  if number[0:2].isalpha():
        code=number[0:2]


  state_codes = (
    "AP", "AR", "AS", "BR", "CG", "GA", "GJ", "HR", "HP",
    "JH", "KA", "KL", "MP", "MH", "MN", "ML", "MZ", "NL",
    "OD", "PB", "RJ", "SK", "TN", "TS", "TR", "UP", "UK", 
    "WB"
  )

  states=(
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal" )
  
  if code in state_codes:
        i=state_codes.index(code)
        print("State :",states[i])
  else:
     print("invalid State")   

  return code    

def district(number,code):
  
  if number[2:4].isnumeric():
     rto=number[2:4]    
    
  rto_codes = {
    "AP": {
        "01": "Srikakulam",
        "02": "Vizianagaram",
        "03": "Visakhapatnam",
        "04": "Kakinada",
        "05": "Dr. B. R. Ambedkar Konaseema",
        "06": "East Godavari",
        "07": "Guntur",
        "08": "Bapatla",
        "09": "Eluru",
        "10": "Krishna",
        "11": "NTR",
        "12": "Prakasam",
        "13": "Palnadu",
        "14": "Nandyal",
        "15": "Kurnool",
        "16": "Sri Sathya Sai",
        "21": "Anantapuramu",
        "22": "Annamayya",
        "23": "Tirupati",
        "24": "Chittoor",
        "26": "YSR Kadapa",
        "27": "Alluri Sitharama Raju",
        "30": "Parvathipuram Manyam",
        "31": "Srikakulam (Additional RTO)",
        "35": "Nellore",
        "37": "Nandyal (Additional RTO)",
        "39": "Tirupati (Additional RTO)"
    },

    "TS": {
        "01": "Adilabad",
        "02": "Karimnagar",
        "03": "Warangal",
        "04": "Khammam",
        "05": "Nalgonda",
        "06": "Mahabubnagar",
        "07": "Ranga Reddy",
        "08": "Medchal-Malkajgiri",
        "09": "Hyderabad Central",
        "10": "Hyderabad North",
        "11": "Hyderabad East",
        "12": "Hyderabad South",
        "13": "Hyderabad West",
        "14": "Reserved",
        "15": "Sangareddy",
        "16": "Nizamabad",
        "17": "Kamareddy",
        "18": "Nirmal",
        "19": "Mancherial",
        "20": "Komaram Bheem Asifabad",
        "21": "Jagtial",
        "22": "Peddapalli",
        "23": "Rajanna Sircilla",
        "24": "Jayashankar Bhupalpally",
        "25": "Mulugu",
        "26": "Mahabubabad",
        "27": "Siddipet",
        "28": "Medak",
        "29": "Sangareddy (Additional)",
        "30": "Vikarabad",
        "31": "Nagarkurnool",
        "32": "Wanaparthy",
        "33": "Jogulamba Gadwal",
        "34": "Narayanpet",
        "35": "Suryapet",
        "36": "Yadadri Bhuvanagiri"
      },

    "KA": {
        "01": "Bengaluru Central",
        "02": "Bengaluru West",
        "03": "Bengaluru East",
        "04": "Bengaluru North",
        "05": "Bengaluru South",
        "06": "Tumakuru",
        "07": "Kolar",
        "08": "KGF",
        "09": "Mysuru West",
        "10": "Chamrajnagar",
        "11": "Mandya",
        "12": "Madikeri",
        "13": "Hassan",
        "14": "Shivamogga",
        "15": "Sagara",
        "16": "Chitradurga",
        "17": "Davanagere",
        "18": "Chikkamagaluru",
        "19": "Mangaluru",
        "20": "Udupi",
        "21": "Puttur",
        "22": "Belagavi",
        "23": "Chikkodi",
        "24": "Bailhongal",
        "25": "Dharwad",
        "26": "Gadag",
        "27": "Haveri",
        "28": "Vijayapura",
        "29": "Bagalkot",
        "30": "Karwar",
        "31": "Sirsi",
        "32": "Kalaburagi",
        "33": "Yadgir",
        "34": "Ballari",
        "35": "Hospet",
        "36": "Raichur",
        "37": "Koppal",
        "38": "Bidar",
        "39": "Bhalki",
        "40": "Chikkaballapur",
        "41": "Ramanagara",
        "42": "Ramdurg",
        "43": "Hubballi"
    },

    "TN": {
        "01": "Chennai Central",
        "02": "Chennai North West",
        "03": "Chennai North East",
        "04": "Chennai East",
        "05": "Chennai North",
        "06": "Mandaveli",
        "07": "Thiruvanmiyur",
        "09": "Kanchipuram",
        "10": "Chengalpattu",
        "11": "Tambaram",
        "18": "Red Hills",
        "19": "Chengalpattu South",
        "20": "Tiruvallur",
        "21": "Kanchipuram West",
        "22": "Meenambakkam",
        "23": "Vellore",
        "24": "Krishnagiri",
        "25": "Tiruvannamalai",
        "28": "Namakkal",
        "29": "Dharmapuri",
        "30": "Salem West",
        "31": "Cuddalore",
        "32": "Villupuram",
        "33": "Erode",
        "34": "Tiruchengode",
        "36": "Gobichettipalayam",
        "37": "Coimbatore South",
        "38": "Coimbatore North",
        "39": "Tiruppur North",
        "40": "Mettupalayam",
        "41": "Pollachi",
        "42": "Tiruppur South",
        "43": "Ooty",
        "45": "Tiruchirappalli",
        "58": "Madurai South",
        "66": "Coimbatore Central"
    },

    "KL": {
        "01": "Thiruvananthapuram",
        "02": "Kollam",
        "03": "Pathanamthitta",
        "04": "Alappuzha",
        "05": "Kottayam",
        "06": "Idukki",
        "07": "Ernakulam",
        "08": "Thrissur",
        "09": "Palakkad",
        "10": "Malappuram",
        "11": "Kozhikode",
        "12": "Wayanad",
        "13": "Kannur",
        "14": "Kasaragod",
        "15": "Kochi",
        "16": "Attingal",
        "17": "Muvattupuzha",
        "18": "Vadakara",
        "19": "Parassala",
        "20": "Neyyattinkara",
        "21": "Nedumangad",
        "22": "Kazhakkoottam"
    },
    
    "MH": {
        "01": "Mumbai Central",
        "02": "Mumbai West",
        "03": "Mumbai East",
        "04": "Thane",
        "05": "Kalyan",
        "06": "Raigad",
        "07": "Sindhudurg",
        "08": "Ratnagiri",
        "09": "Kolhapur",
        "10": "Sangli",
        "11": "Satara",
        "12": "Pune",
        "13": "Solapur",
        "14": "Pimpri-Chinchwad",
        "15": "Nashik",
        "16": "Ahmednagar",
        "17": "Shrirampur",
        "18": "Dhule",
        "19": "Jalgaon",
        "20": "Aurangabad",
        "21": "Jalna",
        "22": "Parbhani",
        "23": "Beed",
        "24": "Latur",
        "25": "Osmanabad",
        "26": "Nanded",
        "27": "Amravati",
        "28": "Buldhana",
        "29": "Yavatmal",
        "30": "Akola",
        "31": "Nagpur",
        "32": "Wardha",
        "33": "Gadchiroli",
        "34": "Chandrapur",
        "35": "Gondia",
        "36": "Bhandara",
        "37": "Washim",
        "38": "Hingoli",
        "39": "Nandurbar",
        "40": "Wadi (Nagpur)"
    },

    "GJ": {
        "01": "Ahmedabad",
        "02": "Mehsana",
        "03": "Rajkot",
        "04": "Bhavnagar",
        "05": "Surat",
        "06": "Vadodara",
        "07": "Nadiad",
        "08": "Palanpur",
        "09": "Himmatnagar",
        "10": "Jamnagar",
        "11": "Junagadh",
        "12": "Bhuj",
        "13": "Surendranagar",
        "14": "Amreli",
        "15": "Valsad",
        "16": "Bharuch",
        "17": "Godhra",
        "18": "Gandhinagar",
        "19": "Bardoli",
        "20": "Dahod",
        "21": "Navsari",
        "22": "Anand",
        "23": "Patan",
        "24": "Porbandar",
        "25": "Rajpipla",
        "26": "Vyara",
        "27": "Modasa",
        "28": "Veraval",
        "29": "Botad",
        "30": "Morbi",
        "31": "Aravalli",
        "32": "Dwarka"
    },

    "GA": {
        "01": "Panaji",
        "02": "Margao",
        "03": "Mapusa",
        "04": "Bicholim",
        "05": "Ponda",
        "06": "Vasco da Gama",
        "07": "Pernem",
        "08": "Quepem",
        "09": "Curchorem",
        "10": "Canacona",
        "11": "Valpoi",
        "12": "Old Goa"
    },

    "UP": {
        "11": "Saharanpur",
        "12": "Muzaffarnagar",
        "13": "Bulandshahr",
        "14": "Ghaziabad",
        "15": "Meerut",
        "16": "Noida (Gautam Buddha Nagar)",
        "17": "Baghpat",
        "19": "Shamli",
        "20": "Bijnor",
        "21": "Moradabad",
        "22": "Rampur",
        "23": "Jyotiba Phule Nagar",
        "24": "Badaun",
        "25": "Bareilly",
        "26": "Pilibhit",
        "27": "Shahjahanpur",
        "30": "Hardoi",
        "31": "Lakhimpur Kheri",
        "32": "Lucknow",
        "33": "Raebareli",
        "34": "Sitapur",
        "35": "Unnao",
        "36": "Amethi",
        "41": "Bahraich",
        "42": "Gonda",
        "43": "Faizabad (Ayodhya)",
        "44": "Barabanki",
        "45": "Ambedkar Nagar",
        "46": "Sultanpur",
        "50": "Azamgarh",
        "51": "Basti",
        "52": "Deoria",
        "53": "Gorakhpur",
        "54": "Mau",
        "55": "Siddharth Nagar",
        "56": "Maharajganj",
        "57": "Padrauna (Kushinagar)",
        "58": "Sant Kabir Nagar",
        "60": "Ballia",
        "61": "Ghazipur",
        "62": "Jaunpur",
        "63": "Mirzapur",
        "64": "Sonbhadra",
        "65": "Varanasi",
        "66": "Bhadohi",
        "67": "Chandauli",
        "70": "Prayagraj",
        "71": "Fatehpur",
        "72": "Pratapgarh",
        "73": "Kaushambi",
        "75": "Kanpur Nagar",
        "76": "Kanpur Dehat"
    },

    "RJ": {
        "01": "Ajmer",
        "02": "Alwar",
        "03": "Banswara",
        "04": "Barmer",
        "05": "Bharatpur",
        "06": "Bhilwara",
        "07": "Bikaner",
        "08": "Bundi",
        "09": "Chittorgarh",
        "10": "Churu",
        "11": "Dholpur",
        "12": "Dungarpur",
        "13": "Sri Ganganagar",
        "14": "Jaipur",
        "15": "Jaisalmer",
        "16": "Jalore",
        "17": "Jhalawar",
        "18": "Jhunjhunu",
        "19": "Jodhpur",
        "20": "Kota",
        "21": "Nagaur",
        "22": "Pali",
        "23": "Sikar",
        "24": "Sirohi",
        "25": "Sawai Madhopur",
        "26": "Tonk",
        "27": "Udaipur"
    },

    "PB": {
        "01": "Amritsar",
        "02": "Bathinda",
        "03": "Faridkot",
        "04": "Ferozepur",
        "05": "Gurdaspur",
        "06": "Hoshiarpur",
        "07": "Jalandhar",
        "08": "Kapurthala",
        "09": "Ludhiana",
        "10": "Patiala",
        "11": "Rupnagar",
        "12": "Sangrur",
        "13": "Nawanshahr",
        "14": "Moga",
        "15": "Fatehgarh Sahib",
        "16": "Muktsar",
        "17": "Barnala",
        "18": "Mohali",
        "19": "Mansa",
        "20": "Pathankot"
    },

    "HR": {
        "01": "Ambala",
        "02": "Yamunanagar",
        "03": "Panchkula",
        "04": "Naraingarh",
        "05": "Karnal",
        "06": "Panipat",
        "07": "Kurukshetra",
        "08": "Kaithal",
        "09": "Guhla",
        "10": "Sonepat",
        "11": "Gohana",
        "12": "Rohtak",
        "13": "Jhajjar",
        "14": "Bahadurgarh",
        "15": "Meham",
        "16": "Bhiwani",
        "17": "Siwani",
        "18": "Loharu",
        "19": "Charkhi Dadri",
        "20": "Hisar",
        "21": "Hansi",
        "22": "Fatehabad",
        "23": "Tohana",
        "24": "Sirsa",
        "25": "Dabwali",
        "26": "Gurugram",
        "27": "Nuh",
        "28": "Faridabad",
        "29": "Palwal",
        "30": "Mahendragarh",
        "31": "Rewari",
        "32": "Narnaul",
        "33": "Jind"
    },

    "HP": {
        "01": "Shimla",
        "02": "Solan",
        "03": "Mandi",
        "04": "Kangra",
        "05": "Hamirpur",
        "06": "Kullu",
        "07": "Una",
        "08": "Chamba",
        "09": "Bilaspur",
        "10": "Sirmaur",
        "11": "Kinnaur",
        "12": "Lahaul and Spiti"
    },

    "MP": {
        "03": "Bhopal",
        "04": "Vidisha",
        "05": "Hoshangabad",
        "06": "Morena",
        "07": "Gwalior",
        "08": "Guna",
        "09": "Indore",
        "10": "Khargone",
        "11": "Dhar",
        "12": "Khandwa",
        "13": "Ujjain",
        "14": "Mandsaur",
        "15": "Sagar",
        "16": "Chhatarpur",
        "17": "Rewa",
        "18": "Shahdol",
        "19": "Satna",
        "20": "Jabalpur",
        "21": "Katni",
        "22": "Seoni",
        "28": "Neemuch",
        "30": "Bhind",
        "37": "Balaghat",
        "41": "Dewas",
        "50": "Railway (Bhopal)"
    },

    "CG": {
        "04": "Raipur",
        "05": "Dhamtari",
        "06": "Mahasamund",
        "07": "Durg",
        "08": "Rajnandgaon",
        "09": "Kawardha",
        "10": "Bilaspur",
        "11": "Janjgir-Champa",
        "12": "Korba",
        "13": "Raigarh",
        "14": "Jashpur",
        "15": "Ambikapur",
        "16": "Baikunthpur",
        "17": "Jagdalpur",
        "18": "Dantewada",
        "19": "Kanker"
    },

    "BR": {
        "01": "Patna",
        "02": "Gaya",
        "03": "Bhojpur",
        "04": "Chapra",
        "05": "Motihari",
        "06": "Muzaffarpur",
        "07": "Darbhanga",
        "08": "Munger",
        "09": "Begusarai",
        "10": "Bhagalpur",
        "11": "Purnia",
        "19": "Nalanda",
        "21": "Nawada",
        "32": "Madhepura",
        "33": "Saharsa"
    },

    "JH": {
        "01": "Ranchi",
        "02": "Hazaribagh",
        "03": "Daltonganj",
        "04": "Dumka",
        "05": "Jamshedpur",
        "06": "Chaibasa",
        "07": "Gumla",
        "08": "Lohardaga",
        "09": "Bokaro",
        "10": "Dhanbad",
        "11": "Giridih",
        "15": "Deoghar",
        "18": "Ramgarh",
        "19": "Pakur",
        "20": "Koderma"
    },

    "WB": {
        "01": "Kolkata",
        "02": "Kolkata",
        "03": "Barrackpore",
        "04": "Howrah",
        "05": "Hooghly",
        "06": "Bankura",
        "07": "Birbhum",
        "08": "Burdwan",
        "09": "Darjeeling",
        "10": "Cooch Behar",
        "11": "Jalpaiguri",
        "12": "Malda",
        "13": "Murshidabad",
        "14": "Nadia",
        "15": "North 24 Parganas",
        "16": "West Midnapore",
        "17": "Purulia",
        "18": "South 24 Parganas"
    },

    "OD": {
        "02": "Bhubaneswar",
        "03": "Balasore",
        "04": "Cuttack",
        "05": "Kalahandi",
        "06": "Koraput",
        "07": "Ganjam",
        "08": "Sambalpur",
        "09": "Keonjhar",
        "10": "Mayurbhanj",
        "11": "Phulbani",
        "12": "Rayagada",
        "13": "Puri",
        "14": "Rourkela",
        "15": "Bhadrak",
        "16": "Baripada",
        "17": "Jharsuguda",
        "18": "Bolangir",
        "19": "Nabarangpur",
        "20": "Nayagarh"
    },

    "AS": {
        "01": "Guwahati (Kamrup)",
        "02": "Nagaon",
        "03": "Jorhat",
        "04": "Sivasagar",
        "05": "Golaghat",
        "06": "Dibrugarh",
        "07": "Lakhimpur",
        "08": "Dhemaji",
        "09": "Sonitpur",
        "10": "Karimganj",
        "11": "Cachar",
        "12": "Hailakandi",
        "13": "Darrang",
        "14": "Nalbari",
        "15": "Barpeta",
        "16": "Kokrajhar",
        "17": "Dhubri",
        "18": "Goalpara",
        "19": "Bongaigaon",
        "20": "Tinsukia"
    },

    "AR": {
        "01": "Itanagar",
        "02": "Naharlagun",
        "03": "Tawang",
        "04": "Bomdila",
        "05": "Seppa",
        "06": "Ziro",
        "07": "Daporijo",
        "08": "Aalo",
        "09": "Pasighat",
        "10": "Anini",
        "11": "Tezu",
        "12": "Changlang",
        "13": "Khonsa"
    },

    "MN": {
        "01": "Imphal West",
        "02": "Imphal East",
        "03": "Churachandpur",
        "04": "Thoubal",
        "05": "Bishnupur",
        "06": "Senapati",
        "07": "Ukhrul",
        "08": "Tamenglong",
        "09": "Chandel"
    },

    "ML": {
        "05": "Shillong",
        "06": "Jowai",
        "07": "Williamnagar",
        "08": "Nongstoin",
        "09": "Tura",
        "10": "Baghmara"
    },

    "MZ": {
        "01": "Aizawl",
        "02": "Lunglei",
        "03": "Saiha",
        "04": "Champhai",
        "05": "Kolasib",
        "06": "Serchhip",
        "07": "Lawngtlai",
        "08": "Mamit"
    },

    "NL": {
        "01": "Kohima",
        "02": "Mokokchung",
        "03": "Tuensang",
        "04": "Mon",
        "05": "Wokha",
        "06": "Zunheboto",
        "07": "Dimapur",
        "08": "Phek"
    },

    "SK": {
        "01": "Gangtok",
        "02": "Gyalshing",
        "03": "Mangan",
        "04": "Namchi"
    },

    "TR": {
        "01": "Agartala",
        "02": "Kailashahar",
        "03": "Udaipur",
        "04": "Dharmanagar",
        "05": "Ambassa",
        "06": "Khowai"
    },

    "UK": {
        "07": "Dehradun",
        "08": "Rishikesh",
        "09": "Rudrapur",
        "10": "Haldwani",
        "11": "Pithoragarh",
        "12": "Almora",
        "13": "Bageshwar",
        "14": "Champawat",
        "15": "Nainital",
        "16": "Haridwar",
        "17": "Roorkee",
        "18": "Udham Singh Nagar"
    }
  }
  
  if code in rto_codes and rto in rto_codes[code]:
     print("District :",rto_codes[code][rto])
    
def series(number):

    number=number.upper()

    if number[4:6].isalpha():
        s=number[4:6]
        s1=number[4:5]
        s2=number[5:6]

    series_number= ord(s1)-ord(s2)  

    print("Series Code :",s)

    return series_number

def vehicle(number,order):
    o=int(order)
    if number[6:11].isnumeric():
        n=number[6:11]

    n=int(n)
    

    vehicle_number=(o*9999)+n

    print("Vehicle Number :",n)

    return vehicle_number     

# def number(number):
#     print(number)

 

def main():
   
    plate = input("Enter your number plate: ")

    plate=plate.strip()
    plate=plate.replace(" ","")

    if len(plate)==10:  
        dis=state(plate)
        district(plate,dis)
        p=series(plate)
        v=vehicle(plate,p)
        # number(v)
    else:
        print("Entered number plate is invalid!!")

main()        



 
 

  