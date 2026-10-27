from __future__ import annotations

import html
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Silent Sounds",
    page_icon="🎶",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).parent
AUDIO_PATH = ROOT / "Audio_Samples.ogg" / "Thumari_By_Gauhar_Jaan_Recorded_in_1905 (1).ogg"

STATES_BY_REGION = {
    "North": ["Himachal Pradesh", "Punjab", "Rajasthan", "Uttar Pradesh", "Uttarakhand", "Haryana"],
    "Central": ["Chhattisgarh", "Madhya Pradesh"],
    "West": ["Goa", "Gujarat", "Maharashtra"],
    "South": ["Andhra Pradesh", "Karnataka", "Kerala", "Tamil Nadu", "Telangana"],
    "East": ["Bihar", "Jharkhand", "Odisha", "West Bengal"],
    "North East": ["Arunachal Pradesh", "Assam", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Sikkim", "Tripura"],
    "Union Territories": [
        "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
        "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry",
    ],
}

MAP_MARKERS = {
    "Jammu and Kashmir": ("JK", 26.0, 13.3), "Ladakh": ("LA", 39.0, 8.6),
    "Himachal Pradesh": ("HP", 40.0, 19.1), "Punjab": ("PB", 29.0, 22.9),
    "Chandigarh": ("CH", 34.0, 25.8), "Haryana": ("HR", 39.0, 29.7),
    "Uttarakhand": ("UK", 51.0, 27.7), "Delhi": ("DL", 41.0, 31.5),
    "Rajasthan": ("RJ", 23.0, 39.3), "Uttar Pradesh": ("UP", 51.0, 37.3),
    "Bihar": ("BR", 66.0, 38.2), "Sikkim": ("SK", 74.0, 32.5),
    "Arunachal Pradesh": ("AR", 88.0, 31.5), "Assam": ("AS", 80.0, 43.9),
    "Meghalaya": ("ML", 78.0, 46.8), "Nagaland": ("NL", 89.0, 42.0),
    "Manipur": ("MN", 91.0, 47.7), "Tripura": ("TR", 82.0, 50.6),
    "Mizoram": ("MZ", 86.0, 54.4), "West Bengal": ("WB", 73.0, 45.8),
    "Jharkhand": ("JH", 66.0, 45.8), "Odisha": ("OD", 67.0, 53.4),
    "Chhattisgarh": ("CG", 56.0, 49.6), "Madhya Pradesh": ("MP", 42.0, 46.8),
    "Gujarat": ("GJ", 19.0, 50.6), "Dadra and Nagar Haveli and Daman and Diu": ("DN", 27.0, 57.3),
    "Maharashtra": ("MH", 39.0, 56.3), "Goa": ("GA", 36.0, 66.9),
    "Telangana": ("TS", 53.0, 59.2), "Andhra Pradesh": ("AP", 56.0, 67.8),
    "Karnataka": ("KA", 43.0, 67.8), "Kerala": ("KL", 42.0, 78.1),
    "Tamil Nadu": ("TN", 51.0, 80.2), "Puducherry": ("PY", 58.0, 76.4),
    "Lakshadweep": ("LD", 12.0, 61.1), "Andaman and Nicobar Islands": ("AN", 86.0, 75.4),
}

# Open-license images from Wikimedia Commons (direct URLs)
INSTRUMENTS = [
    {"id": "sitar-north", "name": "Sitar", "script": "सितार", "states": ["Uttar Pradesh", "Delhi", "West Bengal", "Rajasthan"], "family": "String", "status": "In use", "era": "Medieval", "description": "A long-necked plucked string instrument central to Hindustani classical music. Its sympathetic strings create a distinctive resonant voice.", "source": "https://en.wikipedia.org/wiki/Sitar", "frequency": 196.00, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Sitar3.jpg/640px-Sitar3.jpg", "image_credit": "Sathyadeep", "image_license": "Public Domain"},
    {"id": "tabla-north", "name": "Tabla", "script": "तबला", "states": ["Uttar Pradesh", "Delhi", "Punjab", "Rajasthan"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A pair of hand drums used across Hindustani and other South Asian music traditions.", "source": "https://en.wikipedia.org/wiki/Tabla", "frequency": 164.81, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Tabla_and_bayan.jpg/640px-Tabla_and_bayan.jpg", "image_credit": "Wikimedia", "image_license": "CC BY-SA"},
    {"id": "bansuri-north", "name": "Bansuri", "script": "बांसुरी", "states": ["Uttar Pradesh", "Rajasthan", "Assam", "West Bengal"], "family": "Wind", "status": "In use", "era": "Undated tradition", "description": "A side-blown bamboo flute used in multiple Indian musical traditions.", "source": "https://en.wikipedia.org/wiki/Bansuri", "frequency": 349.23, "image": "https://upload.wikimedia.org/wikipedia/commons/0/02/Bansuri_bamboo_flute_23inch.jpg", "image_credit": "Wikimedia", "image_license": "CC BY-SA"},
    {"id": "mridangam-south", "name": "Mridangam", "script": "மிருதங்கம்", "states": ["Tamil Nadu", "Karnataka", "Andhra Pradesh", "Kerala"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A double-headed barrel drum central to Carnatic concert percussion.", "source": "https://en.wikipedia.org/wiki/Mridangam", "frequency": 130.81, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Mridangam.jpg/640px-Mridangam.jpg", "image_credit": "Wikimedia", "image_license": "CC BY-SA"},
    {"id": "nadaswaram-tamil-nadu", "name": "Nadaswaram", "script": "நாதஸ்வரம்", "states": ["Tamil Nadu", "Puducherry"], "family": "Wind", "status": "In use", "era": "Undated tradition", "description": "A double-reed instrument with a strong presence in South Indian classical and ceremonial music.", "source": "https://en.wikipedia.org/wiki/Nadaswaram", "frequency": 261.63, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Nadaswaram_%28also_nagaswaram_or_nagasuram%29.jpg/640px-Nadaswaram_%28also_nagaswaram_or_nagasuram%29.jpg", "image_credit": "Ashwin Kamath", "image_license": "CC BY 2.0", "audio": "static/audio/nadaswaram-temple.ogg", "audio_credit": "Vis M", "audio_license": "CC BY 4.0", "audio_source": "https://commons.wikimedia.org/wiki/File:Thakil_%26_Nadaswaram_during_temple_Deeparadhana.ogg"},
    {"id": "chenda-kerala", "name": "Chenda", "script": "ചെണ്ട", "states": ["Kerala"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A cylindrical percussion instrument heard in Kerala's temple and ensemble traditions.", "source": "https://en.wikipedia.org/wiki/Chenda", "frequency": 146.83, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/3_Chenda_kept_together-_vijayan_rajapuram.jpg/640px-3_Chenda_kept_together-_vijayan_rajapuram.jpg", "image_credit": "Vijayanrajapuram", "image_license": "CC BY-SA 4.0", "audio": "static/audio/chenda-melam.ogg", "audio_credit": "Alexabraham22da", "audio_license": "CC BY-SA 3.0", "audio_source": "https://commons.wikimedia.org/wiki/File:Chenda_Melam.ogg"},
    {"id": "sarod-north", "name": "Sarod", "script": "सरोद", "states": ["Uttar Pradesh", "West Bengal", "Delhi"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "A plucked, fretless string instrument used in Hindustani classical music.", "source": "https://en.wikipedia.org/wiki/Sarod", "frequency": 220.00, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Sarod.jpg/640px-Sarod.jpg", "image_credit": "Wikimedia", "image_license": "CC BY-SA"},
    {"id": "santoor-jammu-kashmir", "name": "Santoor", "script": "संतूर", "states": ["Jammu and Kashmir"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "A hammered dulcimer with a well-known place in Kashmiri and Hindustani musical contexts.", "source": "https://en.wikipedia.org/wiki/Santoor", "frequency": 293.66, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Indian_santoor.jpg/640px-Indian_santoor.jpg", "image_credit": "Opus88888", "image_license": "CC BY-SA 3.0"},
    {"id": "ektara-west-bengal", "name": "Ektara", "script": "একতারা", "states": ["West Bengal", "Assam", "Bihar", "Jharkhand"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "A one-string folk instrument used in several regional traditions.", "source": "https://en.wikipedia.org/wiki/Ektara", "frequency": 220.00, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Ektara%2C_playing%2C_front_view.png/640px-Ektara%2C_playing%2C_front_view.png", "image_credit": "Drs. FAM Welman", "image_license": "CC BY-SA 4.0"},
    {"id": "ravanhatta-rajasthan", "name": "Ravanhatta", "script": "रावणहत्था", "states": ["Rajasthan"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "A bowed string instrument associated with folk performance in Rajasthan.", "source": "https://en.wikipedia.org/wiki/Ravanhatta", "frequency": 220.00, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Musician_Playing_Ravanhatta_at_Mehrangarh%2C_Rajasthan%2C_India.jpg/640px-Musician_Playing_Ravanhatta_at_Mehrangarh%2C_Rajasthan%2C_India.jpg", "image_credit": "Harshil Mehta", "image_license": "CC BY-SA 4.0"},
    {"id": "ghumot-goa", "name": "Ghumot", "script": "घुमट", "states": ["Goa"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A Goan percussion instrument used in local ensemble traditions.", "source": "https://en.wikipedia.org/wiki/Ghumot", "frequency": 174.61, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Ghumot%2C_the_traditional_drum_of_Goa.jpeg/640px-Ghumot%2C_the_traditional_drum_of_Goa.jpeg", "image_credit": "Wikimedia", "image_license": "CC BY-SA"},
    {"id": "pepa-assam", "name": "Pepa", "script": "প্যাঁপা", "states": ["Assam"], "family": "Wind", "status": "In use", "era": "Undated tradition", "description": "A buffalo-horn wind instrument associated with Bihu music in Assam.", "source": "https://en.wikipedia.org/wiki/Pepa_(instrument)", "frequency": 293.66, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Pepa_%28musical_instrument_made_of_cow_or_buffalo_horn%29_from_Assam.jpg/640px-Pepa_%28musical_instrument_made_of_cow_or_buffalo_horn%29_from_Assam.jpg", "image_credit": "Bengalis in Ahmedabad", "image_license": "CC BY 3.0"},
    {"id": "pung-manipur", "name": "Pung", "script": "পুং", "states": ["Manipur"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "The pung is a barrel drum central to the devotional and performance traditions of Manipur.", "source": "https://en.wikipedia.org/wiki/Pung", "frequency": 196.00, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Pung_Cholom_Manipur.jpg/640px-Pung_Cholom_Manipur.jpg", "image_credit": "Ramesh Lalwani", "image_license": "CC BY 2.0"},
    {"id": "shehnai-north", "name": "Shehnai", "script": "शहनाई", "states": ["Uttar Pradesh", "Bihar", "Rajasthan"], "family": "Wind", "status": "In use", "era": "Undated tradition", "description": "A double-reed wind instrument heard in North Indian classical and ceremonial contexts.", "source": "https://en.wikipedia.org/wiki/Shehnai", "frequency": 293.66, "image": None},
    {"id": "sarangi-north", "name": "Sarangi", "script": "सारंगी", "states": ["Rajasthan", "Uttar Pradesh", "Punjab", "Jammu and Kashmir"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "A bowed string instrument with several regional forms and performance lineages.", "source": "https://en.wikipedia.org/wiki/Sarangi", "frequency": 196.00, "image": None},
    {"id": "veena-south", "name": "Veena", "script": "वीणा", "states": ["Tamil Nadu", "Karnataka", "Andhra Pradesh", "Kerala"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "Veena names several plucked string instruments across South Asian traditions.", "source": "https://en.wikipedia.org/wiki/Veena", "frequency": 261.63, "image": None},
    {"id": "ghatam-south", "name": "Ghatam", "script": "घटम्", "states": ["Tamil Nadu", "Karnataka", "Andhra Pradesh"], "family": "Idiophone", "status": "In use", "era": "Undated tradition", "description": "A clay pot used as a percussion instrument in South Indian music.", "source": "https://en.wikipedia.org/wiki/Ghatam", "frequency": 196.00, "image": None},
    {"id": "thavil-tamil-nadu", "name": "Thavil", "script": "தவில்", "states": ["Tamil Nadu", "Puducherry"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A barrel-shaped percussion instrument played in South Indian ensemble music.", "source": "https://en.wikipedia.org/wiki/Thavil", "frequency": 174.61, "image": None},
    {"id": "kanjira-tamil-nadu", "name": "Kanjira", "script": "கஞ்சிரா", "states": ["Tamil Nadu", "Puducherry"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A small frame drum used in South Indian percussion.", "source": "https://en.wikipedia.org/wiki/Kanjira", "frequency": 164.81, "image": None},
    {"id": "morsing-tamil-nadu", "name": "Morsing", "script": "மோர்சிங்", "states": ["Tamil Nadu", "Karnataka"], "family": "Idiophone", "status": "In use", "era": "Undated tradition", "description": "A jew's harp used as a rhythmic instrument in South Indian music.", "source": "https://en.wikipedia.org/wiki/Morsing", "frequency": 220.00, "image": None},
    {"id": "algoza-punjab", "name": "Algoza", "script": "ਅਲਗੋਜ਼ਾ", "states": ["Punjab", "Rajasthan"], "family": "Wind", "status": "In use", "era": "Undated tradition", "description": "A paired-flute instrument heard in Punjabi and Rajasthani folk music.", "source": "https://en.wikipedia.org/wiki/Algoza", "frequency": 246.94, "image": None},
    {"id": "tumbi-punjab", "name": "Tumbi", "script": "ਤੂੰਬੀ", "states": ["Punjab"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "A plucked, single-string folk instrument associated with Punjabi music.", "source": "https://en.wikipedia.org/wiki/Tumbi", "frequency": 246.94, "image": None},
    {"id": "khartal-rajasthan", "name": "Khartal", "script": "खड़ताल", "states": ["Rajasthan"], "family": "Idiophone", "status": "In use", "era": "Undated tradition", "description": "Handheld clappers used rhythmically in folk and devotional performance.", "source": "https://en.wikipedia.org/wiki/Khartal", "frequency": 329.63, "image": None},
    {"id": "dhol-north", "name": "Dhol", "script": "ढोल", "states": ["Punjab", "Rajasthan", "Gujarat", "Maharashtra", "Assam"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A large double-headed barrel drum used across many Indian regions.", "source": "https://en.wikipedia.org/wiki/Dhol", "frequency": 110.00, "image": None},
    {"id": "manjira-north", "name": "Manjira", "script": "मंजीरा", "states": ["Rajasthan", "Uttar Pradesh", "Maharashtra", "Gujarat"], "family": "Idiophone", "status": "In use", "era": "Undated tradition", "description": "Small hand cymbals used to keep rhythm in folk and classical settings.", "source": "https://en.wikipedia.org/wiki/Manjira", "frequency": 523.25, "image": None},
    {"id": "gogona-assam", "name": "Gogona", "script": "গগণা", "states": ["Assam"], "family": "Idiophone", "status": "In use", "era": "Undated tradition", "description": "A bamboo jaw harp of Assam, closely linked to Bihu.", "source": "https://en.wikipedia.org/wiki/Gogona", "frequency": 329.63, "image": None},
    {"id": "pena-manipur", "name": "Pena", "script": "পেনা", "states": ["Manipur"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "A bowed string instrument associated with Meitei music in Manipur.", "source": "https://en.wikipedia.org/wiki/Pena_(instrument)", "frequency": 220.00, "image": None},
    {"id": "pakhawaj-north", "name": "Pakhawaj", "script": "पखावज", "states": ["Uttar Pradesh", "Rajasthan", "Madhya Pradesh"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A barrel drum associated with North Indian classical and devotional repertoire.", "source": "https://en.wikipedia.org/wiki/Pakhavaj", "frequency": 146.83, "image": None},
    {"id": "mizhavu-kerala", "name": "Mizhavu", "script": "മിഴാവ്", "states": ["Kerala"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A large copper percussion instrument associated with performance traditions in Kerala.", "source": "https://en.wikipedia.org/wiki/Mizhavu", "frequency": 110.00, "image": None},
    {"id": "dilruba-north", "name": "Dilruba", "script": "दिलरुबा", "states": ["Punjab", "Haryana", "Uttar Pradesh"], "family": "String", "status": "In use", "era": "Medieval", "description": "A bowed instrument with frets and a skin-covered resonator.", "source": "https://en.wikipedia.org/wiki/Dilruba", "frequency": 220.00, "image": None},
    {"id": "esraj-west-bengal", "name": "Esraj", "script": "এসরাজ", "states": ["West Bengal", "Bihar"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "A bowed string instrument with frets, popular in Bengal.", "source": "https://en.wikipedia.org/wiki/Esraj", "frequency": 196.00, "image": None},
    {"id": "dotara-bengal", "name": "Dotara", "script": "দোতারা", "states": ["West Bengal", "Assam", "Bihar"], "family": "String", "status": "In use", "era": "Undated tradition", "description": "A multi-string plucked folk instrument of Bengal and Assam.", "source": "https://en.wikipedia.org/wiki/Dotara", "frequency": 246.94, "image": None},
    {"id": "khol-assam", "name": "Khol", "script": "খোল", "states": ["Assam", "West Bengal", "Manipur"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A double-headed clay drum associated with Vaishnavite traditions.", "source": "https://en.wikipedia.org/wiki/Khol", "frequency": 130.81, "image": None},
    {"id": "jal-tarang", "name": "Jal Tarang", "script": "जल तरंग", "states": ["Uttar Pradesh", "Rajasthan", "Maharashtra"], "family": "Idiophone", "status": "Rare", "era": "Medieval", "description": "A set of ceramic bowls filled with water and struck with sticks.", "source": "https://en.wikipedia.org/wiki/Jal_tarang", "frequency": 261.63, "image": None},
    {"id": "kamaicha-rajasthan", "name": "Kamaicha", "script": "कमायचा", "states": ["Rajasthan"], "family": "String", "status": "Rare", "era": "Undated tradition", "description": "A bowed string instrument of the Manganiyar community of Rajasthan.", "source": "https://en.wikipedia.org/wiki/Kamaicha", "frequency": 196.00, "image": None},
    {"id": "rudra-veena", "name": "Rudra Veena", "script": "रुद्र वीणा", "states": ["Uttar Pradesh", "Rajasthan", "Madhya Pradesh"], "family": "String", "status": "Rare", "era": "Ancient", "description": "A large fretted stick zither associated with dhrupad.", "source": "https://en.wikipedia.org/wiki/Rudra_veena", "frequency": 110.00, "image": None},
    {"id": "ghungroo", "name": "Ghungroo", "script": "घुँघरू", "states": ["Rajasthan", "Uttar Pradesh", "Maharashtra", "Tamil Nadu"], "family": "Idiophone", "status": "In use", "era": "Undated tradition", "description": "Small bells strung together and worn by dancers.", "source": "https://en.wikipedia.org/wiki/Ghungroo", "frequency": 659.25, "image": None},
    {"id": "harmonium-north", "name": "Harmonium", "script": "हार्मोनियम", "states": ["Uttar Pradesh", "Punjab", "West Bengal", "Maharashtra"], "family": "Wind", "status": "In use", "era": "Colonial", "description": "A free-reed keyboard instrument fully absorbed into Indian music.", "source": "https://en.wikipedia.org/wiki/Pump_organ", "frequency": 261.63, "image": None},
    {"id": "parai-tamil-nadu", "name": "Parai", "script": "பறை", "states": ["Tamil Nadu"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A frame drum associated with Tamil performance traditions.", "source": "https://en.wikipedia.org/wiki/Parai", "frequency": 146.83, "image": None},
    {"id": "dappu-telangana", "name": "Dappu", "script": "డప్పు", "states": ["Telangana", "Andhra Pradesh"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A frame drum used in Telugu-speaking regions.", "source": "https://en.wikipedia.org/wiki/Dappu", "frequency": 164.81, "image": None},
    {"id": "edakka-kerala", "name": "Edakka", "script": "ഇടയ്ക്ക", "states": ["Kerala"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "An hourglass-shaped drum of Kerala temple music.", "source": "https://en.wikipedia.org/wiki/Idakka", "frequency": 174.61, "image": None},
    {"id": "maddale-karnataka", "name": "Maddale", "script": "ಮದ್ದಳೆ", "states": ["Karnataka"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A double-headed drum central to Yakshagana theatre of coastal Karnataka.", "source": "https://en.wikipedia.org/wiki/Maddale", "frequency": 146.83, "image": None},
    {"id": "chimta-punjab", "name": "Chimta", "script": "ਚਿਮਟਾ", "states": ["Punjab", "Haryana", "Rajasthan"], "family": "Idiophone", "status": "In use", "era": "Undated tradition", "description": "A metallic tongs-like instrument with jingles, used in Punjabi folk music.", "source": "https://en.wikipedia.org/wiki/Chimta", "frequency": 392.00, "image": None},
    {"id": "nagada-central", "name": "Nagada", "script": "नगाड़ा", "states": ["Rajasthan", "Madhya Pradesh", "Uttar Pradesh", "Gujarat"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "Large kettle drums traditionally used for announcements and processions.", "source": "https://en.wikipedia.org/wiki/Naqqara", "frequency": 98.00, "image": None},
    {"id": "surbahar-north", "name": "Surbahar", "script": "सुरबहार", "states": ["Uttar Pradesh", "Delhi", "West Bengal"], "family": "String", "status": "Rare", "era": "Colonial", "description": "A bass sitar designed for deeper, more contemplative playing.", "source": "https://en.wikipedia.org/wiki/Surbahar", "frequency": 130.81, "image": None},
    {"id": "tumbaknari-kashmir", "name": "Tumbaknari", "script": "تمبک ناری", "states": ["Jammu and Kashmir"], "family": "Percussion", "status": "In use", "era": "Undated tradition", "description": "A goblet-shaped drum of Kashmir, used in folk and Sufi contexts.", "source": "https://en.wikipedia.org/wiki/Tumbaknari", "frequency": 164.81, "image": None},
    {"id": "pungi-rajasthan", "name": "Pungi", "script": "पुंगी", "states": ["Rajasthan", "Uttar Pradesh"], "family": "Wind", "status": "In use", "era": "Undated tradition", "description": "A double-reed wind instrument made from a gourd and bamboo pipes.", "source": "https://en.wikipedia.org/wiki/Pungi", "frequency": 293.66, "image": None},
    {"id": "kartal-bengal", "name": "Kartal", "script": "করতাল", "states": ["West Bengal", "Odisha", "Assam"], "family": "Idiophone", "status": "In use", "era": "Undated tradition", "description": "Wooden or metal clappers used in kirtan and folk music of eastern India.", "source": "https://en.wikipedia.org/wiki/Kartal", "frequency": 392.00, "image": None},
]

FAMILIES = ["All families", "String", "Wind", "Percussion", "Idiophone"]
STATUSES = ["All statuses", "In use", "Rare", "Endangered", "Extinct"]
ERAS = ["Any era", "Ancient", "Medieval", "Colonial", "Early modern", "Modern", "Undated tradition"]


def apply_theme(theme: str, immersive: bool = False) -> None:
    dark = theme == "Dark"
    bg = "#0c0f0d" if dark else "#f7f1e6"
    fg = "#f2ebe0" if dark else "#1f1c16"
    muted = "#a39e92" if dark else "#6b655a"
    panel = "#151a16" if dark else "#fffdf9"
    border = "#2c342e" if dark else "#e5dccf"
    accent = "#c9a26a"
    soft = "#c9a26a33" if dark else "#c9a26a22"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700&display=swap');
    :root {{ color-scheme: {'dark' if dark else 'light'}; }}
    [data-testid="stAppViewContainer"] {{
        background: radial-gradient(ellipse at 8% 8%, {'#1c2a20' if dark else '#e8dcc8'} 0%, transparent 32%),
                    radial-gradient(ellipse at 92% 22%, {'#1a241c' if dark else '#ebe3d4'} 0%, transparent 30%), {bg};
        color: {fg};
        transition: background 0.4s ease;
    }}
    [data-testid="stHeader"] {{ background: transparent; }}
    [data-testid="stSidebar"] {{ background: {panel}; border-right: 1px solid {border}; min-width: 300px !important; }}
    [data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
        background: radial-gradient(ellipse at 20% 0%, {'#2a3a2e' if dark else '#ebe0c8'} 0%, transparent 48%), linear-gradient(180deg, {panel}, {bg});
    }}
    [data-testid="stSidebar"] [role="radiogroup"] {{ border-left: 2px solid {accent}55; padding-left: 12px; }}
    .sidebar-brand {{ padding: 16px 4px 18px; border-bottom: 1px solid {border}; margin-bottom: 14px; text-align: center; }}
    .sidebar-sigil {{ color: {accent}; font: 44px/1 'Cormorant Garamond', Georgia, serif; text-shadow: 0 0 24px {soft}; }}
    .sidebar-title {{ margin: 4px 0 0; color: {fg}; font: 600 24px/1.1 'Cormorant Garamond', Georgia, serif; }}
    .sidebar-subtitle {{ margin-top: 5px; color: {muted}; font: 500 10px 'DM Mono', monospace; letter-spacing: .14em; text-transform: uppercase; }}
    .sidebar-quote {{ margin: 12px 4px 16px; padding: 10px 12px; color: {muted}; font: italic 14px/1.5 'Cormorant Garamond', Georgia, serif; border-left: 2px solid {accent}66; background: {'#1a221c88' if dark else '#f5efe688'}; border-radius: 0 6px 6px 0; }}
    .pin-board {{ display: flex; flex-direction: column; gap: 10px; margin: 6px 0 14px; }}
    .pin {{ background: {panel}; border: 1px solid {border}; border-radius: 10px; overflow: hidden; box-shadow: 0 3px 14px {'#00000030' if dark else '#3d2e1a10'}; transition: transform .25s cubic-bezier(.2,.8,.2,1), box-shadow .25s ease; }}
    .pin:hover {{ transform: translateY(-3px); box-shadow: 0 10px 24px {'#00000050' if dark else '#3d2e1a18'}; }}
    .pin-header {{ height: 64px; display: grid; place-items: center; background: radial-gradient(ellipse at 70% 30%, {accent}30 0%, transparent 55%), linear-gradient(145deg, {'#243028' if dark else '#f0e6d4'}, {'#1a221c' if dark else '#e8dcc8'}); }}
    .pin-glyph {{ font: 32px/1 'Cormorant Garamond', Georgia, serif; color: {accent}; }}
    .pin-body {{ padding: 10px 12px 12px; }}
    .pin-label {{ font: 500 9px 'DM Mono', monospace; letter-spacing: .12em; text-transform: uppercase; color: {accent}; margin-bottom: 3px; }}
    .pin-title {{ font: 600 15px/1.25 'Cormorant Garamond', Georgia, serif; color: {fg}; margin: 0 0 3px; }}
    .pin-meta {{ font: 11.5px/1.35 'Manrope', sans-serif; color: {muted}; }}
    html, body, [class*="css"] {{ font-family: 'Manrope', sans-serif; color: {fg}; }}
    h1, h2, h3 {{ font-family: 'Cormorant Garamond', Georgia, serif !important; color: {fg} !important; font-weight: 600 !important; }}
    .block-container {{ max-width: 1420px; padding-top: 1rem; padding-bottom: 3.5rem; }}
    [data-testid="stMetric"] {{ background: {panel}; border: 1px solid {border}; padding: 0.95rem 1.05rem; border-radius: 10px; transition: transform .2s ease; }}
    [data-testid="stMetric"]:hover {{ transform: translateY(-2px); }}
    [data-testid="stButton"] button {{ border-radius: 8px; transition: transform .2s cubic-bezier(.2,.8,.2,1), border-color .2s, box-shadow .2s; font-family: 'Manrope', sans-serif !important; }}
    [data-testid="stButton"] button:hover {{ transform: translateY(-2px); border-color: {accent}; box-shadow: 0 6px 16px {soft}; }}
    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{ background: {panel}; border-color: {border}; border-radius: 8px; }}
    .section-label {{ margin: 0 0 6px; color: {accent}; font: 500 11px 'DM Mono', monospace; letter-spacing: .12em; text-transform: uppercase; }}
    .instrument-card {{
        min-height: 160px; padding: 0; border: 1px solid {border}; background: {panel};
        border-radius: 12px; overflow: hidden; box-shadow: 0 8px 22px {'#00000025' if dark else '#3d2e1a0c'};
        transition: transform .28s cubic-bezier(.2,.8,.2,1), box-shadow .28s ease, border-color .25s;
        animation: cardIn .5s ease both;
    }}
    .instrument-card:hover {{ transform: translateY(-5px); border-color: {accent}66; box-shadow: 0 16px 36px {'#00000040' if dark else '#3d2e1a16'}; }}
    .card-img {{ width: 100%; height: 160px; object-fit: cover; display: block; transition: transform .4s ease; }}
    .instrument-card:hover .card-img {{ transform: scale(1.04); }}
    .card-body {{ padding: 14px 16px 16px; }}
    .instrument-mark {{ color: {accent}; font: 28px/1 'Cormorant Garamond', Georgia, serif; }}
    .small-muted {{ color: {muted}; font-size: 12px; }}
    .footer-note {{ color: {muted}; font-size: 12px; border-top: 1px solid {border}; padding-top: 14px; margin-top: 22px; }}
    .india-map-wrap {{ display: flex; justify-content: center; margin: 6px 0 12px; }}
    @keyframes cardIn {{ from {{ opacity: 0; transform: translateY(18px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    {('[data-testid="stSidebar"], [data-testid="stHeader"] {{ display: none; }} .block-container {{ max-width: none; padding: 0 10px 10px; }}' if immersive else '')}
    </style>
    """, unsafe_allow_html=True)


def get_instrument(instrument_id: str) -> dict:
    return next(item for item in INSTRUMENTS if item["id"] == instrument_id)


def navigate(page: str, instrument_id: str | None = None) -> None:
    st.session_state.page_navigation = page
    if instrument_id:
        st.session_state.selected_instrument = instrument_id


def render_home_intro(animate: bool) -> None:
    intro = f"""<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>
    *{{box-sizing:border-box}}body{{margin:0;background:transparent;color:#f1ece2;font-family:'Cormorant Garamond',Georgia,serif}}
    .intro{{position:relative;min-height:300px;padding:44px clamp(20px,5vw,72px);overflow:hidden;border-radius:12px;
      background:radial-gradient(ellipse at 78% 46%,#73613d50,transparent 36%),radial-gradient(ellipse at 26% 110%,#25423470,transparent 48%),linear-gradient(120deg,#0d100e,#151c16 54%,#101412)}}
    .intro::before{{content:'♪';position:absolute;right:12%;top:-20px;color:#d4ad6c18;font-size:220px;transform:rotate(12deg);transition:transform 8s ease}}
    .kicker{{color:#d7b574;font:11px 'DM Mono',monospace;letter-spacing:.15em;text-transform:uppercase}}
    h1{{position:relative;z-index:1;margin:18px 0 12px;font-size:clamp(40px,6.5vw,78px);font-weight:500;line-height:1.04}}
    .cursor{{display:inline-block;width:2px;height:.85em;margin-left:4px;background:#d7b574;vertical-align:-.04em;animation:blink .8s step-end infinite}}
    .quote{{position:relative;z-index:1;margin:18px 0 0;color:#d8d1c5;font-size:clamp(15px,2vw,20px);font-style:italic;opacity:0;transform:translateY(10px);animation:rise .7s .2s ease-out forwards}}
    .sub{{position:relative;z-index:1;max-width:540px;margin:10px 0 0;color:#a8aca4;font:13px/1.65 Manrope,Arial,sans-serif;opacity:0;animation:rise .65s .5s ease-out forwards}}
    @keyframes blink{{50%{{opacity:0}}}}@keyframes rise{{to{{opacity:1;transform:translateY(0)}}}}
    @media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;opacity:1!important;transform:none!important}}}}
    </style></head><body><main class="intro"><div class="kicker">An archive of India's living musical heritage</div>
    <h1 aria-label="Silent Sounds"><span id="title"></span><span class="cursor" id="cursor"></span></h1>
    <p class="quote">“A sound remembered is a tradition still breathing.”</p>
    <p class="sub">Listen closely. Find the instrument. Follow its story home.</p></main>
    <script>const t='Silent Sounds',el=document.getElementById('title'),c=document.getElementById('cursor');
    const red=matchMedia('(prefers-reduced-motion: reduce)').matches;let i=0;
    if(!{str(animate).lower()}||red){{el.textContent=t;c.style.display='none'}}
    else{{const go=()=>{{el.textContent=t.slice(0,i++);if(i<=t.length)setTimeout(go,95);else c.style.display='none'}};setTimeout(go,250)}}</script></body></html>"""
    st.iframe(intro, height=310, width="stretch")


def render_interactive_map(selected_state: str) -> None:
    markers = []
    for state, (abbr, left, top) in MAP_MARKERS.items():
        sel = " selected" if selected_state == state else ""
        markers.append(
            f'<button type="button" class="marker{sel}" data-state="{html.escape(state, quote=True)}" '
            f'title="{html.escape(state, quote=True)}" style="left:{left}%;top:{top}%">{abbr}</button>'
        )
    map_html = f"""<style>
        .india-map{{position:relative;width:min(100%,520px);aspect-ratio:736/805;margin:0 auto;overflow:hidden;border:1px solid #91866e40;border-radius:12px;
      background:radial-gradient(ellipse at 50% 40%,#4a634850 0%,transparent 55%),linear-gradient(155deg,#121a15,#0c100e);
      box-shadow:0 14px 32px #00000040,inset 0 0 50px #00000030}}
        .map-image{{position:absolute;inset:0;width:100%;height:100%;object-fit:fill;border-radius:11px}}
    .marker{{position:absolute;z-index:3;display:grid;place-items:center;width:28px;height:28px;transform:translate(-50%,-50%);
      border:1.5px solid #dec18d;background:linear-gradient(145deg,#2a3a30,#1c2820);color:#f5eee2;border-radius:50%;
      font:600 9.5px 'DM Mono',monospace;cursor:pointer;box-shadow:0 2px 8px #0008;
      transition:transform .22s cubic-bezier(.2,.8,.2,1),background .22s,box-shadow .22s}}
    .marker:hover,.marker:focus-visible{{z-index:5;transform:translate(-50%,-50%) scale(1.38);background:linear-gradient(145deg,#9e3b30,#7a2e24);border-color:#ffe0a6;box-shadow:0 0 0 4px #c99d6030,0 6px 16px #0009}}
    .marker.selected{{background:linear-gradient(145deg,#b04438,#8c322d);border-color:#ffe0a6;box-shadow:0 0 0 4px #c99d6030,0 3px 12px #0009;transform:translate(-50%,-50%) scale(1.15)}}
    @media(max-width:600px){{.india-map{{width:min(100%,360px)}}.marker{{width:24px;height:24px;font-size:8.5px}}}}
    </style>
    <div class="india-map"><img class="map-image" src="/app/static/india-map.jpg" alt="User-provided illustrated map of India with state boundaries" loading="eager">{''.join(markers)}</div>
    <script>document.querySelectorAll('.india-map .marker').forEach(b=>b.addEventListener('click',()=>{{const u=new URL(location.href);u.searchParams.set('state',b.dataset.state);location.assign(u)}}))</script>"""
    st.markdown('<div class="india-map-wrap">', unsafe_allow_html=True)
    st.html(map_html, unsafe_allow_javascript=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_selector() -> None:
    st.markdown('<p class="section-label">01 / Choose a region</p>', unsafe_allow_html=True)
    st.markdown("## Find your way through the sound map")
    current = st.session_state.get("selected_state", "All India")
    all_states = sorted(s for states in STATES_BY_REGION.values() for s in states)
    render_interactive_map(current)
    selected = st.selectbox("Find a state or Union Territory", ["All India", *all_states],
                            index=["All India", *all_states].index(current) if current in ["All India", *all_states] else 0, key="map_search")
    if selected != current:
        st.session_state.selected_state = selected
    st.caption("Click a marker or use the search above.")


def render_library() -> None:
    st.markdown('<p class="section-label">02 / The listening room</p>', unsafe_allow_html=True)
    st.markdown("## Instruments, carried forward")
    selected_state = st.session_state.get("selected_state", "All India")
    c1, c2, c3 = st.columns(3)
    with c1: family = st.selectbox("Family", FAMILIES, key="family_filter")
    with c2: status = st.selectbox("Status", STATUSES, key="status_filter")
    with c3: era = st.selectbox("Era", ERAS, key="era_filter")

    items = INSTRUMENTS
    if selected_state != "All India": items = [i for i in items if selected_state in i["states"]]
    if family != "All families": items = [i for i in items if i["family"] == family]
    if status != "All statuses": items = [i for i in items if i["status"] == status]
    if era != "Any era": items = [i for i in items if i["era"] == era]

    st.caption(f"{len(items)} catalog entries · Starter collection")
    if not items:
        st.info("No verified entries match these filters yet.")
        return

    for start in range(0, len(items), 3):
        cols = st.columns(3, gap="medium")
        for col, item in zip(cols, items[start:start+3]):
            with col:
                img_html = ""
                if item.get("image"):
                    img_html = f'<img class="card-img" src="{html.escape(item["image"])}" alt="{html.escape(item["name"])}" loading="lazy"/>'
                else:
                    img_html = f'<div style="height:160px;display:grid;place-items:center;background:linear-gradient(145deg,#243028,#1a221c);"><span class="instrument-mark" style="font-size:48px">{html.escape(item["script"])}</span></div>'
                st.markdown(f"""
                <div class="instrument-card">
                  {img_html}
                  <div class="card-body">
                    <div class="small-muted">{html.escape(item['family'].upper())} · {html.escape(item['status'].upper())}</div>
                    <h3 style="margin:6px 0 4px;font-size:20px">{html.escape(item['name'])}</h3>
                    <div class="small-muted">{' · '.join(html.escape(s) for s in item['states'][:2])}{'…' if len(item['states'])>2 else ''}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
                st.button("Enter listening room ↗", key=f"open-{item['id']}", width="stretch",
                          on_click=navigate, args=("Listening room", item["id"]))


def render_sound_stage(item: dict) -> None:
    safe_name = html.escape(item["name"])
    safe_script = html.escape(item["script"])
    family = item["family"]
    base = float(item["frequency"])
    img_block = f'<img src="{html.escape(item["image"])}" style="max-height:200px;border-radius:8px;margin:8px 0" alt="{safe_name}"/>' if item.get("image") else f'<div class="glyph">{safe_script}</div>'
    audio_path = ROOT / item["audio"] if item.get("audio") else None
    recording_url = f"/app/static/audio/{audio_path.name}" if audio_path and audio_path.is_file() else ""
    auto_label = "▶ Play recording" if recording_url else "▶ Play study"
    stage_label = "Licensed instrument recording · reactive playback" if recording_url else "Sound study · Web Audio synthesis"
    audio_credit = f"{item['audio_credit']} · {item['audio_license']}" if recording_url else "Synthesized · not an authentic recording"
    stage = f"""<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>
    *{{box-sizing:border-box}}body{{margin:0;background:#080a09;color:#f1eee8;font:14px Manrope,sans-serif}}
    .stage{{height:calc(100vh - 20px);min-height:580px;position:relative;overflow:hidden;background:radial-gradient(ellipse at 50% 48%,#374737 0%,#182019 34%,#080a09 78%);display:flex;align-items:center;justify-content:center;text-align:center}}
    canvas{{position:absolute;inset:0;width:100%;height:100%;opacity:.7;z-index:0}}
    .content{{position:relative;z-index:1;display:grid;place-items:center;gap:12px;padding:18px}}
    .curtain{{position:absolute;z-index:4;top:0;bottom:0;width:51%;pointer-events:none;background:repeating-linear-gradient(90deg,#3b0a11 0 11px,#68111c 12px 24px,#8d2730 25px 31px,#5b0d17 32px 45px);box-shadow:inset 0 0 55px #160407;transform:scaleX(1);animation:curtain-open 1.65s cubic-bezier(.68,0,.2,1) .25s forwards}}
    .curtain::after{{content:'';position:absolute;top:0;bottom:0;width:5px;background:linear-gradient(90deg,#d8b576,#71421f,#e2c482);opacity:.65}}
    .curtain.left{{left:0;transform-origin:left center}} .curtain.left::after{{right:0}}
    .curtain.right{{right:0;transform-origin:right center}}
    @keyframes curtain-open{{to{{transform:scaleX(0)}}}}
    .glyph{{font:140px 'Cormorant Garamond',Georgia,serif;color:#d9b780;text-shadow:0 0 40px #bd8f5260;line-height:1}}
    .name{{font:40px 'Cormorant Garamond',Georgia,serif}}
    .hint{{color:#a7aaa2;max-width:400px;line-height:1.55;font-size:13px}}
    .controls{{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}}
    button{{border:1px solid #596159;background:#1a211c;color:#f1eee8;padding:11px 16px;border-radius:6px;font:inherit;cursor:pointer;transition:border-color .2s,transform .15s}}
    button:hover{{border-color:#d9b780;transform:translateY(-1px)}}
    @media(prefers-reduced-motion:reduce){{.curtain{{animation-duration:.01ms;animation-delay:0s}}}}
    .status{{color:#d9b780;font:11px 'DM Mono',monospace;min-height:16px}}
    .tag{{font:10px 'DM Mono',monospace;text-transform:uppercase;letter-spacing:.12em;color:#a7aaa2}}
    </style></head><body>
    <main class="stage" id="stage"><canvas id="glow"></canvas><div class="curtain left" aria-hidden="true"></div><div class="curtain right" aria-hidden="true"></div>
    <div class="content">
    <div class="tag">{stage_label}</div>
      {img_block}
      <div class="name">{safe_name}</div>
      <div class="hint">Interactive mode: tap the stage or press A–G keys. This is a synthesized study, not an authentic recording.</div>
      <div class="controls">
        <button id="auto">{auto_label}</button>
        <button id="interactive">♫ Interactive</button>
        <button id="stop">■ Stop</button>
      </div>
    <div class="tag">{html.escape(audio_credit)}</div>
      <div class="status" id="status">Sound begins only after your gesture.</div>
    </div></main>
    <script>
    const base={base}, family='{family}';
    const canvas=document.getElementById('glow'), ctx=canvas.getContext('2d'), status=document.getElementById('status');
    let audio=null, analyser=null, master=null, recording=null, recordingNode=null, raf=0, oscs=[], timers=[], interactive=false;
    function resize(){{const d=Math.min(devicePixelRatio||1,2);canvas.width=canvas.clientWidth*d;canvas.height=canvas.clientHeight*d;ctx.setTransform(d,0,0,d,0,0)}}
    new ResizeObserver(resize).observe(canvas);resize();
    function init(){{if(!audio){{audio=new(AudioContext||webkitAudioContext)();analyser=audio.createAnalyser();analyser.fftSize=256;master=audio.createGain();master.gain.value=.32;master.connect(analyser);analyser.connect(audio.destination)}}if(audio.state==='suspended')audio.resume()}}
    function clear(){{timers.forEach(clearTimeout);timers=[];oscs.forEach(o=>{{try{{o.stop()}}catch{{}}}});oscs=[];if(recording){{recording.pause();try{{recording.currentTime=0}}catch{{}}}}cancelAnimationFrame(raf)}}
    function note(f,d=.5){{init();const n=audio.currentTime,o=audio.createOscillator(),g=audio.createGain(),fl=audio.createBiquadFilter();
      o.type=family==='String'?'sawtooth':family==='Wind'?'triangle':'sine';fl.type='lowpass';fl.frequency.value=family==='Wind'?2400:family==='String'?1700:1000;
      if(family==='Percussion'){{o.frequency.setValueAtTime(f*1.6,n);o.frequency.exponentialRampToValueAtTime(Math.max(50,f*.5),n+Math.min(.15,d*.55))}}
      else{{o.frequency.setValueAtTime(f,n)}}
      g.gain.setValueAtTime(.0001,n);g.gain.exponentialRampToValueAtTime(.55,n+.02);g.gain.exponentialRampToValueAtTime(.0001,n+d);
      o.connect(fl);fl.connect(g);g.connect(master);o.start(n);o.stop(n+d+.02);
      o.onended=()=>{{oscs=oscs.filter(x=>x!==o);if(!oscs.length)cancelAnimationFrame(raf)}};oscs.push(o);
      status.textContent='Playing synthesized '+family.toLowerCase()+' study';animate()}}
    function stop(){{clear();if(master&&audio){{const n=audio.currentTime;master.gain.cancelScheduledValues(n);master.gain.setTargetAtTime(.0001,n,.02)}};status.textContent='Stopped'}}
    function seq(){{clear();init();interactive=false;master.gain.setValueAtTime(.32,audio.currentTime);
      [1,1.25,1.5,1.25,1.12,1.5,1.335,1].forEach((v,i)=>timers.push(setTimeout(()=>note(base*v,.4),i*450)))}}
    function playRecording(){{if(!'{recording_url}'){{seq();return}}clear();init();interactive=false;if(!recording){{recording=new Audio();recording.preload='none';recordingNode=audio.createMediaElementSource(recording);recordingNode.connect(analyser);recording.addEventListener('ended',()=>{{status.textContent='Recording finished'}});recording.addEventListener('error',()=>{{status.textContent='Recording could not be loaded'}})}}recording.src='{recording_url}';recording.load();recording.currentTime=0;recording.play().then(()=>{{status.textContent='Playing licensed recording';animate()}}).catch(()=>{{status.textContent='Tap play again to allow audio'}})}}
    function animate(){{cancelAnimationFrame(raf);const data=new Uint8Array(analyser.frequencyBinCount);
      const draw=()=>{{raf=requestAnimationFrame(draw);analyser.getByteFrequencyData(data);let e=0;for(let i=0;i<data.length;i++)e+=data[i];e=e/data.length/255;
        const w=canvas.clientWidth,h=canvas.clientHeight;ctx.clearRect(0,0,w,h);
        for(let l=0;l<3;l++){{ctx.beginPath();for(let x=0;x<=w;x+=8){{const a=(16+e*90)*(1+l*.3);const y=h*.53+Math.sin(x*.009+performance.now()*.0005+l*1.6)*a;
          x===0?ctx.moveTo(x,y):ctx.lineTo(x,y)}}ctx.strokeStyle=`rgba(${{l===1?'194,151,91':'93,137,107'}},${{.07+e*.2}})`;ctx.lineWidth=18+l*14;ctx.shadowBlur=24+e*70;ctx.shadowColor='#9b8057';ctx.stroke()}}}};draw()}}
    const keys={{a:1,b:1.122,c:1.189,d:1.335,e:1.498,f:1.587,g:1.782}};
    document.addEventListener('keydown',e=>{{const m=keys[e.key.toLowerCase()];if(interactive&&m)note(base*m,.38)}});
    document.getElementById('stage').addEventListener('pointerdown',e=>{{if(interactive&&e.target.tagName!=='BUTTON'){{const r=canvas.getBoundingClientRect();note(base*Math.max(.5,Math.min(2,(e.clientX-r.left)/r.width*1.5)),.42)}}}});
    document.getElementById('auto').onclick=playRecording;
    document.getElementById('interactive').onclick=()=>{{clear();init();interactive=true;status.textContent='Interactive · tap or press A–G';note(base,.3)}};
    document.getElementById('stop').onclick=stop;
    </script></body></html>"""
    st.iframe(stage, height="stretch", width="stretch", alt=f"Full-screen {item['name']} instrument stage")


def render_listening_room() -> None:
    iid = st.session_state.get("selected_instrument")
    if not iid:
        st.info("Choose an instrument from the listening room first.")
        return
    item = get_instrument(iid)
    st.markdown(f'<p class="section-label">LISTENING ROOM / {html.escape(item["family"].upper())}</p>', unsafe_allow_html=True)
    st.markdown(f"## {item['name']} <span style='color:#c9a26a'>{item['script']}</span>", unsafe_allow_html=True)
    st.caption("Sourced catalog entry. Historical details remain provisional where the cited source is incomplete.")
    st.markdown(f"**{item['family']} · {item['status']} · {', '.join(item['states'])}**")
    st.markdown(item["description"])
    if item.get("image_credit"):
        st.caption(f"Image: {item.get('image_credit')} · {item.get('image_license', '')}")
    st.markdown(f"[Instrument reference]({item['source']})")
    render_sound_stage(item)


def render_sidebar_pins() -> None:
    pins = [
        ("∿", "Archive", "Living catalog", "Sourced · open · growing"),
        ("♪", "Sound", "Study, not replica", "Synthesized studies labeled"),
        ("◈", "Map", "36 regions", "Click a marker to filter"),
        ("✧", "Ethics", "Gaps stay visible", "No invented records"),
    ]
    html_pins = ['<div class="pin-board">']
    for g, lab, title, meta in pins:
        html_pins.append(f'<div class="pin"><div class="pin-header"><span class="pin-glyph">{g}</span></div><div class="pin-body"><div class="pin-label">{lab}</div><div class="pin-title">{title}</div><div class="pin-meta">{meta}</div></div></div>')
    html_pins.append('</div>')
    st.markdown(''.join(html_pins), unsafe_allow_html=True)


def main() -> None:
    qs = st.query_params.get("state")
    valid = {s for states in STATES_BY_REGION.values() for s in states}
    if qs in valid:
        st.session_state.selected_state = qs
        st.session_state.map_search = qs
        st.session_state.page_navigation = "Discover"
        st.query_params.clear()

    with st.sidebar:
        st.markdown("<div class='sidebar-brand'><div class='sidebar-sigil'>∿</div><div class='sidebar-title'>Silent Sounds</div><div class='sidebar-subtitle'>An open listening archive</div></div><div class='sidebar-quote'>“Listen long enough, and every place leaves a melody.”</div>", unsafe_allow_html=True)
        theme = st.radio("Appearance", ["Light", "Dark"], horizontal=True, index=0, key="appearance")
        page = st.radio("Explore", ["Discover", "Listening room", "The archive"], key="page_navigation")
        st.markdown("---")
        render_sidebar_pins()
        st.caption("Recordings, images and histories are labeled with their sources.")

    if page == "Listening room":
        apply_theme(theme, immersive=True)
        if st.button("← Return to the map", on_click=navigate, args=("Discover",)):
            st.rerun()
        render_listening_room()
        return

    apply_theme(theme)
    animate = not st.session_state.get("intro_animation_seen", False)
    render_home_intro(animate)
    st.session_state.intro_animation_seen = True

    if page == "Discover":
        render_selector()
        m1, m2, m3 = st.columns(3)
        m1.metric("Regions represented", "36", "28 states · 8 UTs")
        m2.metric("Instruments documented", str(len(INSTRUMENTS)), "Starter collection")
        m3.metric("With images", str(sum(1 for i in INSTRUMENTS if i.get("image"))), "Open-license photos")
        st.divider()
        render_library()
    else:
        st.markdown('<p class="section-label">03 / The archive</p>', unsafe_allow_html=True)
        st.markdown("## A voice from the first recordings")
        if AUDIO_PATH.exists():
            st.caption("Gauhar Jaan · thumri · recorded in 1905")
            st.audio(str(AUDIO_PATH))
        else:
            st.warning("The included audio sample was not found. The rest of the catalog remains available.")
        st.markdown("### What this archive stands for")
        st.write("Silent Sounds is a starter collection, not a finished authority. Instrument records need community review, verified citations, and contributor credit.")
        st.markdown("**Suggest a correction:** include a source, image license, recording rights, and the community or performer to credit.")

    st.markdown('<p class="footer-note">Independent archive prototype · Images from Wikimedia Commons (open licenses) · Sound studies are synthesized and are not historical reconstructions.</p>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()