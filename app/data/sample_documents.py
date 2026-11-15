"""Healthcare knowledge library used by the Research Agent.

General, educational health information (WHO / standard clinical guidance style).
This is a small teaching library, not a substitute for a doctor.
"""

from typing import Any, Dict, List

SAMPLE_DOCUMENTS: List[Dict[str, Any]] = [
    {
        "id": "MED-001",
        "title": "Fever, Cold & Flu: Home Care and Red Flags",
        "category": "Common Illnesses",
        "keywords": ["fever", "temperature", "cold", "flu", "cough", "sore throat", "viral", "influenza", "body ache"],
        "summary": "Self-care for mild viral illness and the signs that mean you should see a doctor.",
        "content": (
            "1. Fever: a body temperature of 38 C (100.4 F) or higher. Normal is about 36.5-37.5 C.\n"
            "2. Most colds, flu and sore throats are viral. Antibiotics do not work on viruses and should only be "
            "taken when a doctor prescribes them.\n"
            "3. Home care: rest, plenty of fluids, light food, warm salt-water gargles for sore throat. "
            "Paracetamol can ease fever and aches if taken exactly as per the label.\n"
            "4. See a doctor if: fever lasts more than 3 days, temperature is 39.5 C or higher, breathing is difficult, "
            "there is chest pain, a stiff neck, confusion, a new rash, persistent vomiting, or signs of dehydration "
            "(very little urine, dizziness, dry mouth).\n"
            "5. Any fever in a baby under 3 months, or a fever in someone with a weak immune system, needs urgent "
            "medical review."
        ),
    },
    {
        "id": "MED-002",
        "title": "High Blood Pressure (Hypertension): Basics and Lifestyle",
        "category": "Heart & Circulation",
        "keywords": ["blood pressure", "hypertension", "bp", "salt", "heart", "systolic", "diastolic", "dash diet"],
        "summary": "What blood pressure numbers mean and evidence-based lifestyle steps.",
        "content": (
            "1. Blood pressure is written as systolic/diastolic (for example 120/80 mmHg). Readings below 120/80 are "
            "considered normal. Hypertension is generally diagnosed when repeated readings are 140/90 or higher "
            "(some guidelines use 130/80). One high reading is not a diagnosis; a doctor confirms with repeat checks.\n"
            "2. Lifestyle measures: keep salt below 5 g (about one teaspoon) per day, eat more fruit, vegetables and "
            "whole grains (DASH-style diet), exercise about 150 minutes a week, maintain a healthy weight, limit "
            "alcohol, and do not smoke or use tobacco.\n"
            "3. Take prescribed blood pressure medicines regularly. Never stop or change them without asking your doctor.\n"
            "4. Emergency: very high blood pressure with severe headache, chest pain, shortness of breath, vision "
            "changes, confusion or weakness needs emergency care."
        ),
    },
    {
        "id": "MED-003",
        "title": "Type 2 Diabetes and Blood Sugar: Symptoms and Targets",
        "category": "Metabolic Health",
        "keywords": ["diabetes", "blood sugar", "glucose", "hba1c", "insulin", "thirst", "hypoglycemia", "sugar"],
        "summary": "Normal sugar ranges, early symptoms, low-sugar first aid, and lifestyle care.",
        "content": (
            "1. Common symptoms: increased thirst, frequent urination, tiredness, blurred vision, slow-healing wounds, "
            "unexplained weight loss. Many people have no symptoms, so screening matters.\n"
            "2. Typical fasting blood glucose: below 100 mg/dL is normal, 100-125 mg/dL is prediabetes, and 126 mg/dL "
            "or higher on repeat tests suggests diabetes. HbA1c of 6.5% or higher also suggests diabetes. Diagnosis "
            "must be confirmed by a doctor.\n"
            "3. Lifestyle: balanced meals with fewer sugary drinks and refined carbohydrates, regular walking or "
            "exercise, weight management, adequate sleep, and regular check-ups (eyes, feet, kidneys).\n"
            "4. Low blood sugar (shakiness, sweating, confusion) in someone on diabetes medicine: take about 15 g "
            "of fast sugar (glucose tablets, juice), recheck after 15 minutes, and seek help if not improving.\n"
            "5. Seek urgent care for vomiting, abdominal pain, fruity-smelling breath, or drowsiness with very high sugar."
        ),
    },
    {
        "id": "MED-004",
        "title": "Safe Use of Common Medicines (Paracetamol, NSAIDs, Antibiotics)",
        "category": "Medicines Safety",
        "keywords": ["paracetamol", "acetaminophen", "ibuprofen", "diclofenac", "nsaid", "antibiotic", "dose", "medicine", "painkiller", "aspirin"],
        "summary": "Key safety rules for over-the-counter pain and fever medicines and antibiotics.",
        "content": (
            "1. Paracetamol: follow the label. For healthy adults the usual maximum is 4 g (4,000 mg) in 24 hours, "
            "and lower for people with liver disease or heavy alcohol use. Many cold and flu combination products "
            "already contain paracetamol, so do not double up.\n"
            "2. NSAIDs (ibuprofen, diclofenac, aspirin) can irritate the stomach and affect kidneys and blood pressure. "
            "Take with food, use the lowest dose for the shortest time, and avoid them with stomach ulcers, kidney "
            "disease, pregnancy, or blood thinners unless a doctor agrees.\n"
            "3. Do not give aspirin to children or teenagers. Children's doses depend on weight; ask a doctor or "
            "pharmacist.\n"
            "4. Antibiotics are only for bacterial infections. Take them exactly as prescribed, finish the course "
            "unless the doctor says otherwise, and never share or reuse leftovers.\n"
            "5. Tell your doctor or pharmacist about allergies and all medicines you take to avoid interactions."
        ),
    },
    {
        "id": "MED-005",
        "title": "First Aid and Emergency Warning Signs",
        "category": "Emergency Care",
        "keywords": ["emergency", "chest pain", "heart attack", "stroke", "bleeding", "burn", "choking", "first aid", "ambulance", "unconscious"],
        "summary": "Recognising emergencies and basic first aid until help arrives.",
        "content": (
            "1. In India call 112 (national emergency number) or 108 (ambulance). Do not drive yourself in an emergency.\n"
            "2. Possible heart attack: chest pressure or pain, spreading to arm, jaw or back, sweating, breathlessness, "
            "nausea. Call for help immediately and keep the person calm and seated.\n"
            "3. Stroke (FAST): Face drooping, Arm weakness, Speech difficulty, Time to call emergency services at once.\n"
            "4. Severe bleeding: press firmly on the wound with a clean cloth and keep pressing; do not remove soaked cloth, "
            "add more on top.\n"
            "5. Burns: cool under clean running water for about 20 minutes; do not apply ice, butter or toothpaste; "
            "cover loosely with a clean non-fluffy cloth.\n"
            "6. Choking with inability to breathe or speak needs immediate back blows and abdominal thrusts and a call for help."
        ),
    },
    {
        "id": "MED-006",
        "title": "Dengue, Malaria and Monsoon Fevers",
        "category": "Infectious Diseases (India)",
        "keywords": ["dengue", "malaria", "mosquito", "monsoon", "platelet", "rash", "chills", "viral fever"],
        "summary": "Recognising mosquito-borne fevers, safe symptom care, and warning signs.",
        "content": (
            "1. Dengue: sudden high fever with severe headache, pain behind the eyes, muscle and joint pain, and "
            "sometimes a rash. Malaria: fever with chills and sweating that may come in cycles. Blood tests are needed "
            "to confirm either illness.\n"
            "2. With suspected dengue, use paracetamol for fever and drink plenty of fluids. Avoid aspirin and "
            "NSAIDs such as ibuprofen or diclofenac because they can raise bleeding risk.\n"
            "3. Dengue warning signs (often when the fever starts to fall, around day 3-7): severe stomach pain, "
            "repeated vomiting, bleeding gums or nose, black stools, extreme tiredness or drowsiness, cold clammy skin. "
            "Go to hospital immediately.\n"
            "4. Prevention: remove stagnant water (coolers, pots, tyres), use mosquito nets and repellents, wear "
            "full-sleeved clothing, and keep surroundings clean."
        ),
    },
    {
        "id": "MED-007",
        "title": "Nutrition, Exercise and Sleep for Healthy Adults",
        "category": "Lifestyle & Prevention",
        "keywords": ["diet", "nutrition", "exercise", "sleep", "weight", "healthy", "water", "fruits", "vegetables", "obesity", "lifestyle"],
        "summary": "WHO-style baseline recommendations for diet, activity and sleep.",
        "content": (
            "1. Eat a variety of foods: at least 400 g (about five portions) of fruit and vegetables daily, whole grains, "
            "pulses, nuts, and limited fried and processed food.\n"
            "2. Limit free sugars to under 10% of daily energy and salt to under 5 g per day.\n"
            "3. Adults should aim for at least 150 minutes of moderate activity (such as brisk walking) per week, "
            "plus muscle-strengthening activity on two days.\n"
            "4. Most adults need 7-9 hours of sleep. Regular sleep times, less screen time before bed, and limiting "
            "caffeine in the evening help.\n"
            "5. Drink enough water through the day, avoid tobacco, and limit alcohol. Attend routine health check-ups "
            "and vaccinations."
        ),
    },
    {
        "id": "MED-008",
        "title": "Stress, Anxiety and Mental Wellbeing",
        "category": "Mental Health",
        "keywords": ["stress", "anxiety", "depression", "mental", "mood", "panic", "worry", "sleep", "counselling", "low mood"],
        "summary": "Everyday coping strategies and when to seek professional mental health support.",
        "content": (
            "1. Stress and anxiety are common. Signs include constant worry, restlessness, poor sleep, irritability, "
            "racing heart and trouble concentrating.\n"
            "2. Helpful habits: regular sleep, daily physical activity, slow breathing exercises, limiting caffeine "
            "and alcohol, staying connected with friends and family, and breaking tasks into small steps.\n"
            "3. Seek professional help if low mood, anxiety or panic lasts more than two weeks or affects study, "
            "work or relationships. Doctors, psychologists and psychiatrists can help, and treatment works.\n"
            "4. If someone has thoughts of harming themselves, contact emergency services (112) or the Tele-MANAS "
            "mental health helpline (14416) right away and stay with them until help arrives."
        ),
    },
]
