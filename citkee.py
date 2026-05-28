#!/usr/bin/env python3
"""
CITKEE Diploma Entrance Mock Test 2026-27
Interactive Python script with 150 multiple choice questions.
"""

import sys

# ------------------------------------------------------------
# Data structure: each question is a dict with keys:
# 'text', 'options' (list of 4 strings), 'answer' (0-3 index for A-D)
# ------------------------------------------------------------

questions = []

# SECTION A: MATHEMATICS (Q1–Q50)
questions.append({"text": "The HCF of 96 and 404 is:", "options": ["4", "8", "12", "16"], "answer": 0})
questions.append({"text": "Which of the following is an irrational number?", "options": ["√16", "√25", "√7", "√49"], "answer": 2})
questions.append({"text": "The decimal expansion of 17/8 is:", "options": ["Terminating", "Non-terminating repeating", "Non-terminating non-repeating", "None of these"], "answer": 0})
questions.append({"text": "The LCM of two numbers is 180 and their HCF is 6. If one number is 18, the other is:", "options": ["30", "60", "45", "90"], "answer": 1})
questions.append({"text": "If p and q are two distinct prime numbers, then their HCF is:", "options": ["pq", "p + q", "1", "p – q"], "answer": 2})
questions.append({"text": "The number of zeroes of the polynomial p(x) = x² – 5x + 6 is:", "options": ["0", "1", "2", "3"], "answer": 2})
questions.append({"text": "If one zero of the polynomial 3x² + 8x + k is the reciprocal of the other, then k =", "options": ["1", "3", "–3", "–1"], "answer": 1})
questions.append({"text": "The zeroes of the polynomial x² – 3 are:", "options": ["±√3", "±3", "±1", "±9"], "answer": 0})
questions.append({"text": "If α and β are zeroes of x² – 4x + 3, then α + β =", "options": ["3", "–4", "4", "–3"], "answer": 2})
questions.append({"text": "A polynomial of degree 3 has at most how many zeroes?", "options": ["1", "2", "3", "4"], "answer": 2})
questions.append({"text": "The pair of equations x = 4 and y = 3 graphically represents:", "options": ["Parallel lines", "Coincident lines", "Lines intersecting at (4, 3)", "Lines intersecting at (3, 4)"], "answer": 2})
questions.append({"text": "The solution of the system: 2x + 3y = 12 and x – y = 1 is:", "options": ["x = 3, y = 2", "x = 2, y = 3", "x = 5, y = 1", "x = 1, y = 5"], "answer": 0})
questions.append({"text": "If the system of equations kx + 3y = 1 and 12x + ky = 2 has no solution, then k =", "options": ["6", "–6", "4", "–4"], "answer": 1})
questions.append({"text": "For what value of k do the equations 2x – ky = 3 and 4x – 6y = 6 have infinitely many solutions?", "options": ["3", "–3", "6", "–6"], "answer": 0})
questions.append({"text": "The sum of digits of a two-digit number is 9. If digits are reversed, the number increases by 27. The number is:", "options": ["36", "45", "27", "63"], "answer": 0})
questions.append({"text": "The roots of 2x² – 5x + 3 = 0 are:", "options": ["1, 3/2", "–1, –3/2", "3/2, 1", "2, 3"], "answer": 2})
questions.append({"text": "The discriminant of x² + 4x + 4 = 0 is:", "options": ["0", "16", "–16", "8"], "answer": 0})
questions.append({"text": "If the roots of ax² + bx + c = 0 are equal, then:", "options": ["b² = 4ac", "b² > 4ac", "b² < 4ac", "b² = ac"], "answer": 0})
questions.append({"text": "The quadratic equation whose roots are 2 and –3 is:", "options": ["x² + x – 6 = 0", "x² – x – 6 = 0", "x² + x + 6 = 0", "x² – x + 6 = 0"], "answer": 1})
questions.append({"text": "A train travels 360 km at a uniform speed. If the speed had been 5 km/h more, it would have taken 1 hour less. The speed is:", "options": ["40 km/h", "30 km/h", "45 km/h", "60 km/h"], "answer": 0})
questions.append({"text": "The 10th term of the AP: 2, 7, 12, ... is:", "options": ["42", "47", "52", "57"], "answer": 1})
questions.append({"text": "The common difference of the AP: –5, –1, 3, 7, ... is:", "options": ["–4", "4", "2", "–2"], "answer": 1})
questions.append({"text": "The sum of first 20 natural numbers is:", "options": ["190", "200", "210", "220"], "answer": 2})
questions.append({"text": "How many terms of the AP 3, 5, 7, ... must be taken to give a sum of 120?", "options": ["8", "10", "12", "15"], "answer": 1})
questions.append({"text": "If the nth term of an AP is 4n – 3, the first term is:", "options": ["1", "4", "–3", "7"], "answer": 0})
questions.append({"text": "The value of sin 30° + cos 60° is:", "options": ["1", "√3/2", "1/2", "√2"], "answer": 0})
questions.append({"text": "If tan θ = 3/4, then sin θ =", "options": ["3/5", "4/5", "3/4", "4/3"], "answer": 0})
questions.append({"text": "The value of (sin²30° + cos²30°) is:", "options": ["0", "2", "1/2", "1"], "answer": 3})
questions.append({"text": "If sin A = cos A, then A =", "options": ["30°", "45°", "60°", "90°"], "answer": 1})
questions.append({"text": "The angle of elevation of a 10m tall tower from a point 10m away is:", "options": ["30°", "60°", "45°", "90°"], "answer": 2})
questions.append({"text": "The distance between points (3, 4) and (0, 0) is:", "options": ["3", "4", "5", "7"], "answer": 2})
questions.append({"text": "The midpoint of the segment joining (2, 6) and (4, 2) is:", "options": ["(3, 4)", "(4, 3)", "(2, 4)", "(6, 8)"], "answer": 0})
questions.append({"text": "The area of triangle with vertices (0,0), (3,0), (0,4) is:", "options": ["6 sq. units", "12 sq. units", "7 sq. units", "10 sq. units"], "answer": 0})
questions.append({"text": "The x-intercept of the line 2x + 3y = 6 is:", "options": ["2", "3", "6", "–3"], "answer": 1})
questions.append({"text": "The section formula for dividing (x₁, y₁) and (x₂, y₂) in ratio m:n internally gives x-coordinate as:", "options": ["(mx₁ + nx₂)/(m + n)", "(mx₂ + nx₁)/(m + n)", "(mx₁ – nx₂)/(m – n)", "(mx₂ – nx₁)/(m – n)"], "answer": 1})
questions.append({"text": "The tangent to a circle at any point is:", "options": ["Parallel to the radius", "Perpendicular to the radius at that point", "Equal to the diameter", "A chord of the circle"], "answer": 1})
questions.append({"text": "Two circles of radii 5 cm and 3 cm touch externally. The distance between their centres is:", "options": ["2 cm", "8 cm", "15 cm", "5 cm"], "answer": 1})
questions.append({"text": "The angle subtended by a diameter at the circumference is:", "options": ["45°", "60°", "90°", "180°"], "answer": 2})
questions.append({"text": "In triangle ABC, if DE || BC and AD/DB = 3/5, then AE/EC =", "options": ["3/5", "5/3", "3/8", "5/8"], "answer": 0})
questions.append({"text": "If two triangles are similar with ratio 1:4, the ratio of their areas is:", "options": ["1:4", "1:16", "1:8", "1:2"], "answer": 1})
questions.append({"text": "The area of a circle with diameter 14 cm is:", "options": ["154 cm²", "44 cm²", "308 cm²", "616 cm²"], "answer": 0})
questions.append({"text": "The total surface area of a cylinder with r = 7 cm and h = 10 cm is:", "options": ["748 cm²", "374 cm²", "440 cm²", "880 cm²"], "answer": 0})
questions.append({"text": "The volume of a cone with r = 3 cm and h = 7 cm is:", "options": ["66 cm³", "33 cm³", "63 cm³", "22 cm³"], "answer": 0})
questions.append({"text": "The surface area of a sphere of radius 7 cm is:", "options": ["616 cm²", "154 cm²", "308 cm²", "132 cm²"], "answer": 0})
questions.append({"text": "The perimeter of a sector of radius 10.5 cm and angle 60° is: (π = 22/7)", "options": ["32 cm", "11 cm", "25 cm", "21 cm"], "answer": 0})
questions.append({"text": "The mean of 3, 7, 11, 15, 19 is:", "options": ["10", "11", "12", "15"], "answer": 1})
questions.append({"text": "The median of the data: 5, 3, 8, 1, 9, 6, 2 is:", "options": ["5", "6", "3", "8"], "answer": 0})
questions.append({"text": "A die is thrown once. The probability of getting a prime number is:", "options": ["1/2", "1/3", "2/3", "1/6"], "answer": 0})
questions.append({"text": "A card is drawn from a well-shuffled deck of 52 cards. The probability that it is a king is:", "options": ["1/13", "4/52", "Both A and B", "1/4"], "answer": 2})
questions.append({"text": "If P(E) = 0.65, then P(E') is:", "options": ["0.65", "1.65", "0.35", "0"], "answer": 2})

# SECTION B: PHYSICS (Q51–Q75)
questions.append({"text": "The SI unit of force is:", "options": ["Joule", "Pascal", "Newton", "Watt"], "answer": 2})
questions.append({"text": "Which physical quantity has the unit kg·m²·s⁻²?", "options": ["Power", "Pressure", "Energy", "Momentum"], "answer": 2})
questions.append({"text": "A car travels 60 km in 2 hours. Its average speed is:", "options": ["120 km/h", "15 km/h", "30 km/h", "45 km/h"], "answer": 2})
questions.append({"text": "The velocity-time graph of uniform motion is:", "options": ["A curve", "A horizontal straight line", "A vertical straight line", "A parabola"], "answer": 1})
questions.append({"text": "A body starts from rest and attains a velocity of 20 m/s in 4 seconds. Its acceleration is:", "options": ["80 m/s²", "5 m/s²", "4 m/s²", "10 m/s²"], "answer": 1})
questions.append({"text": "Distance covered by a body in nth second under uniform acceleration is given by:", "options": ["u + a(n – 1/2)", "un + an²/2", "u + an", "un – an²/2"], "answer": 0})
questions.append({"text": "Newton's first law of motion defines:", "options": ["Force", "Momentum", "Inertia", "Acceleration"], "answer": 2})
questions.append({"text": "The unit of momentum is:", "options": ["kg·m/s", "kg·m/s²", "N·m", "J/s"], "answer": 0})
questions.append({"text": "A 10 kg object is pushed with 50 N force. Its acceleration is:", "options": ["500 m/s²", "5 m/s²", "50 m/s²", "0.5 m/s²"], "answer": 1})
questions.append({"text": "Action and reaction forces act on:", "options": ["Same body in the same direction", "Different bodies", "Same body in opposite directions", "Different bodies in the same direction"], "answer": 1})
questions.append({"text": "The work done by a force at 90° to displacement is:", "options": ["Maximum", "Minimum", "Zero", "Negative"], "answer": 2})
questions.append({"text": "The kinetic energy of a 2 kg object moving at 3 m/s is:", "options": ["6 J", "18 J", "9 J", "3 J"], "answer": 2})
questions.append({"text": "Power is defined as:", "options": ["Work × Time", "Work / Time", "Force × Velocity²", "Energy × Time"], "answer": 1})
questions.append({"text": "1 horsepower is equal to:", "options": ["100 W", "746 W", "1000 W", "500 W"], "answer": 1})
questions.append({"text": "The gravitational force between two masses is inversely proportional to:", "options": ["Their masses", "Distance between them", "Square of distance between them", "Cube of distance between them"], "answer": 2})
questions.append({"text": "The value of g on the surface of the Moon is approximately:", "options": ["1.6 m/s²", "9.8 m/s²", "4.9 m/s²", "0.98 m/s²"], "answer": 0})
questions.append({"text": "The speed of sound in air at 0°C is approximately:", "options": ["330 m/s", "300 m/s", "343 m/s", "360 m/s"], "answer": 0})
questions.append({"text": "Echo is produced due to:", "options": ["Refraction of sound", "Reflection of sound", "Absorption of sound", "Diffraction of sound"], "answer": 1})
questions.append({"text": "The human ear can hear frequencies in the range:", "options": ["0 – 20 Hz", "20 Hz – 20,000 Hz", "20,000 Hz – 200,000 Hz", "1 – 100 Hz"], "answer": 1})
questions.append({"text": "The phenomenon responsible for the twinkling of stars is:", "options": ["Reflection", "Dispersion", "Atmospheric refraction", "Scattering"], "answer": 2})
questions.append({"text": "The power of a lens is –2D. It is a:", "options": ["Convex lens of focal length 50 cm", "Concave lens of focal length 50 cm", "Convex lens of focal length 2 m", "Concave lens of focal length 2 m"], "answer": 1})
questions.append({"text": "Ohm's law states V = IR. If resistance doubles and voltage is constant, current:", "options": ["Doubles", "Halves", "Remains same", "Becomes zero"], "answer": 1})
questions.append({"text": "Three resistors of 2Ω, 3Ω, and 6Ω are connected in parallel. The equivalent resistance is:", "options": ["11Ω", "1Ω", "3Ω", "6Ω"], "answer": 1})
questions.append({"text": "A magnetic field line is a:", "options": ["Straight line always", "Closed loop", "Broken curve", "Spiral"], "answer": 1})
questions.append({"text": "The specific heat capacity of water is:", "options": ["4200 J/kg·K", "1000 J/kg·K", "2100 J/kg·K", "840 J/kg·K"], "answer": 0})

# SECTION C: CHEMISTRY (Q76–Q100)
questions.append({"text": "Which state of matter has a definite volume but no definite shape?", "options": ["Solid", "Liquid", "Gas", "Plasma"], "answer": 1})
questions.append({"text": "The process by which a solid directly converts to gas without passing through liquid state is:", "options": ["Evaporation", "Condensation", "Sublimation", "Fusion"], "answer": 2})
questions.append({"text": "The boiling point of water at standard atmospheric pressure is:", "options": ["0°C", "100°C", "373°C", "273°C"], "answer": 1})
questions.append({"text": "Which of the following is a pure substance?", "options": ["Air", "Sea water", "Milk", "Distilled water"], "answer": 3})
questions.append({"text": "Atomic number of an element represents:", "options": ["Number of neutrons", "Number of protons", "Mass number", "Number of electrons + protons"], "answer": 1})
questions.append({"text": "The valence electrons of chlorine (atomic number 17) are:", "options": ["5", "6", "7", "1"], "answer": 2})
questions.append({"text": "Who proposed the nuclear model of the atom?", "options": ["Bohr", "Rutherford", "Thomson", "Dalton"], "answer": 1})
questions.append({"text": "The element with atomic number 11 belongs to:", "options": ["Group 2, Period 3", "Group 1, Period 3", "Group 17, Period 2", "Group 18, Period 3"], "answer": 1})
questions.append({"text": "In the modern periodic table, elements are arranged in order of:", "options": ["Atomic mass", "Atomic radius", "Atomic number", "Valence electrons"], "answer": 2})
questions.append({"text": "Which of the following has the smallest atomic radius in Period 2?", "options": ["Li", "Be", "N", "Ne"], "answer": 3})
questions.append({"text": "An ionic bond is formed by:", "options": ["Sharing of electrons", "Transfer of electrons", "Sharing of protons", "Transfer of protons"], "answer": 1})
questions.append({"text": "The molecule of water (H₂O) has what type of bonding?", "options": ["Ionic", "Metallic", "Covalent", "Coordinate"], "answer": 2})
questions.append({"text": "Which of the following is a combination reaction?", "options": ["CaCO₃ → CaO + CO₂", "2H₂ + O₂ → 2H₂O", "Fe + CuSO₄ → FeSO₄ + Cu", "AgNO₃ + NaCl → AgCl + NaNO₃"], "answer": 1})
questions.append({"text": "The chemical formula of rust is:", "options": ["Fe₂O₃", "Fe₃O₄", "Fe₂O₃·xH₂O", "FeO"], "answer": 2})
questions.append({"text": "Which gas is liberated when zinc reacts with dilute HCl?", "options": ["O₂", "Cl₂", "H₂", "SO₂"], "answer": 2})
questions.append({"text": "A solution with pH = 2 is:", "options": ["Neutral", "Mildly acidic", "Strongly acidic", "Strongly basic"], "answer": 2})
questions.append({"text": "Baking soda is chemically:", "options": ["Na₂CO₃", "NaHCO₃", "NaCl", "NaOH"], "answer": 1})
questions.append({"text": "Which of the following is the best conductor of electricity among metals?", "options": ["Gold", "Copper", "Silver", "Aluminium"], "answer": 2})
questions.append({"text": "The process of coating iron with zinc to prevent corrosion is called:", "options": ["Tinning", "Anodizing", "Galvanization", "Electroplating"], "answer": 2})
questions.append({"text": "Carbon forms a large number of compounds due to:", "options": ["Its small size", "Catenation and tetravalency", "High melting point", "Metallic character"], "answer": 1})
questions.append({"text": "Which of the following is a saturated hydrocarbon?", "options": ["Ethene", "Ethyne", "Ethane", "Benzene"], "answer": 2})
questions.append({"text": "The functional group –COOH is present in:", "options": ["Alcohol", "Aldehyde", "Carboxylic acid", "Ester"], "answer": 2})
questions.append({"text": "The allotropes of carbon include:", "options": ["Diamond, Graphite, and Buckminsterfullerene", "Diamond, Charcoal only", "Graphite and Coal only", "Coke and Carbon black only"], "answer": 0})
questions.append({"text": "When copper reacts with silver nitrate solution, the colour of the solution:", "options": ["Remains the same", "Turns blue", "Turns colourless", "Turns black"], "answer": 1})
questions.append({"text": "Which gas is produced during photosynthesis?", "options": ["CO₂", "N₂", "O₂", "H₂"], "answer": 2})

# SECTION D: BIOLOGY (Q101–Q125)
questions.append({"text": "The basic structural and functional unit of life is:", "options": ["Tissue", "Organ", "Cell", "Organism"], "answer": 2})
questions.append({"text": "The organelle responsible for cellular respiration is:", "options": ["Chloroplast", "Ribosome", "Mitochondria", "Nucleus"], "answer": 2})
questions.append({"text": "The cell wall of plant cells is made up of:", "options": ["Chitin", "Cellulose", "Peptidoglycan", "Glycogen"], "answer": 1})
questions.append({"text": "Lysosomes are also called:", "options": ["Power house of cell", "Protein factory", "Suicidal bags", "Control centre"], "answer": 2})
questions.append({"text": "Which tissue provides flexibility to the ear and nose?", "options": ["Bone", "Cartilage", "Ligament", "Tendon"], "answer": 1})
questions.append({"text": "Xylem is responsible for transportation of:", "options": ["Food", "Water and minerals", "Oxygen", "Hormones"], "answer": 1})
questions.append({"text": "Guard cells are found in:", "options": ["Roots", "Stems", "Leaves (stomata)", "Flowers"], "answer": 2})
questions.append({"text": "The process of releasing energy from glucose in the absence of oxygen is:", "options": ["Aerobic respiration", "Anaerobic respiration", "Photosynthesis", "Transpiration"], "answer": 1})
questions.append({"text": "The end products of aerobic respiration are:", "options": ["Glucose and Water", "CO₂ and Water", "Alcohol and CO₂", "Lactic acid and CO₂"], "answer": 1})
questions.append({"text": "Which organ produces bile juice?", "options": ["Pancreas", "Stomach", "Liver", "Small intestine"], "answer": 2})
questions.append({"text": "The enzyme responsible for breaking down starch in the mouth is:", "options": ["Pepsin", "Amylase", "Lipase", "Trypsin"], "answer": 1})
questions.append({"text": "The largest artery in the human body is:", "options": ["Pulmonary artery", "Femoral artery", "Carotid artery", "Aorta"], "answer": 3})
questions.append({"text": "Platelets in blood are responsible for:", "options": ["Carrying oxygen", "Fighting infection", "Clotting of blood", "Transporting nutrients"], "answer": 2})
questions.append({"text": "The functional unit of the kidney is:", "options": ["Neuron", "Villus", "Nephron", "Alveolus"], "answer": 2})
questions.append({"text": "The process by which kidneys filter blood is called:", "options": ["Diffusion", "Osmosis", "Ultrafiltration", "Active transport"], "answer": 2})
questions.append({"text": "Vegetative reproduction in Bryophyllum occurs through:", "options": ["Seeds", "Leaf buds", "Runners", "Spores"], "answer": 1})
questions.append({"text": "The male reproductive part of a flower is the:", "options": ["Pistil", "Petal", "Stamen", "Sepal"], "answer": 2})
questions.append({"text": "Binary fission is a method of reproduction in:", "options": ["Amoeba", "Hydra", "Fern", "Yeast"], "answer": 0})
questions.append({"text": "Mendel's law of segregation states that:", "options": ["Characters blend in offspring", "Alleles separate during gamete formation", "All traits are dominant", "Traits are acquired through environment"], "answer": 1})
questions.append({"text": "A cross between two heterozygous tall plants (Tt × Tt) gives tall to dwarf ratio of:", "options": ["1:1", "1:2:1", "3:1", "2:1"], "answer": 2})
questions.append({"text": "Darwin's theory of natural selection is based on:", "options": ["Survival of the weakest", "Inheritance of acquired characters", "Survival of the fittest", "Random mutation only"], "answer": 2})
questions.append({"text": "Ozone layer is present in:", "options": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"], "answer": 1})
questions.append({"text": "A food chain always begins with:", "options": ["Herbivore", "Decomposer", "Carnivore", "Producer (Green plant)"], "answer": 3})
questions.append({"text": "BOD stands for:", "options": ["Biological Oxygen Deficit", "Biochemical Oxygen Demand", "Basic Organic Decomposition", "Biological Organic Demand"], "answer": 1})
questions.append({"text": "Which of the following is a non-biodegradable waste?", "options": ["Vegetable peels", "Paper", "Plastic", "Cotton cloth"], "answer": 2})

# SECTION E: ENGLISH (Q126–Q150)
questions.append({"text": "Choose the correct tense: She ______ to school every day.", "options": ["go", "goes", "went", "is going"], "answer": 1})
questions.append({"text": "Fill in the blank with the correct article: He is ______ honest man.", "options": ["a", "an", "the", "no article"], "answer": 1})
questions.append({"text": "Choose the correct preposition: The book is ______ the table.", "options": ["in", "at", "on", "under"], "answer": 2})
questions.append({"text": "Identify the correct passive voice of: 'The teacher praised the student.'", "options": ["The student is praised by the teacher.", "The student was praised by the teacher.", "The student has been praised by the teacher.", "The student praised by teacher."], "answer": 1})
questions.append({"text": "Convert to indirect speech: He said, 'I am reading a book.'", "options": ["He said that he was reading a book.", "He said that he is reading a book.", "He said that I was reading a book.", "He says that he is reading a book."], "answer": 0})
questions.append({"text": "Choose the correct form: If I ______ a bird, I would fly.", "options": ["am", "was", "were", "had been"], "answer": 2})
questions.append({"text": "The synonym of 'abundant' is:", "options": ["Scarce", "Plentiful", "Limited", "Rare"], "answer": 1})
questions.append({"text": "The antonym of 'transparent' is:", "options": ["Clear", "Visible", "Opaque", "Bright"], "answer": 2})
questions.append({"text": "Identify the error: 'He don't know the answer.'", "options": ["He", "don't", "know", "answer"], "answer": 1})
questions.append({"text": "Choose the correctly spelled word:", "options": ["Recieve", "Receive", "Recive", "Receeve"], "answer": 1})
questions.append({"text": "The plural of 'criterion' is:", "options": ["Criterions", "Criterias", "Criteria", "Critera"], "answer": 2})
questions.append({"text": "Fill in with the correct preposition: She is good ______ mathematics.", "options": ["in", "for", "at", "with"], "answer": 2})
questions.append({"text": "Choose the correct tense: By next year, she ______ her degree.", "options": ["will complete", "will have completed", "completed", "has completed"], "answer": 1})
questions.append({"text": "The word 'benevolent' means:", "options": ["Evil", "Harmful", "Kind and generous", "Jealous"], "answer": 2})
questions.append({"text": "Identify the type of sentence: 'What a beautiful painting this is!'", "options": ["Assertive", "Interrogative", "Exclamatory", "Imperative"], "answer": 2})
questions.append({"text": "Choose the correct active voice of: 'A letter was written by him.'", "options": ["He writes a letter.", "He wrote a letter.", "He has written a letter.", "He had written a letter."], "answer": 1})
questions.append({"text": "Choose the correct sentence:", "options": ["She have eaten her food.", "She has eaten her food.", "She had ate her food.", "She have ate her food."], "answer": 1})
questions.append({"text": "The meaning of the idiom 'to burn the midnight oil' is:", "options": ["To waste resources", "To work late into the night", "To start a fire", "To cook at midnight"], "answer": 1})
questions.append({"text": "Fill in the blank: Neither the students nor the teacher ______ present.", "options": ["were", "are", "was", "have"], "answer": 2})
questions.append({"text": "Choose the correct conjunction: She is intelligent ______ hardworking.", "options": ["but", "or", "and", "so"], "answer": 2})

# Comprehension Passage (Q146–Q150)
passage = "Water is the most essential natural resource. About 71% of Earth's surface is covered with water, but only 3% is freshwater. Of that 3%, nearly 69% is locked in glaciers and polar ice caps, leaving less than 1% available for human use. Industrial pollution, plastic waste, and agricultural runoff are major causes of water contamination. Conserving water and preventing its pollution are critical responsibilities for every citizen."
questions.append({"text": f"Read the passage: {passage}\n\nWhat percentage of Earth's surface is covered with water?", "options": ["50%", "69%", "71%", "31%"], "answer": 2})
questions.append({"text": f"Read the passage: {passage}\n\nWhat fraction of freshwater is locked in glaciers?", "options": ["3%", "69%", "31%", "1%"], "answer": 1})
questions.append({"text": f"Read the passage: {passage}\n\nWhich of the following is NOT mentioned as a cause of water contamination?", "options": ["Industrial pollution", "Plastic waste", "Deforestation", "Agricultural runoff"], "answer": 2})
questions.append({"text": f"Read the passage: {passage}\n\nThe word 'critical' in the passage most nearly means:", "options": ["Harmful", "Extremely important", "Unnecessary", "Moderate"], "answer": 1})
questions.append({"text": f"Read the passage: {passage}\n\nThe passage primarily aims to:", "options": ["Describe the water cycle", "Highlight the importance of water conservation", "Explain properties of glaciers", "Discuss global warming"], "answer": 1})

# ------------------------------------------------------------
# Interactive test runner
# ------------------------------------------------------------
def run_test():
    print("\n" + "="*60)
    print("CITKEE DIPLOMA ENTRANCE MOCK TEST 2026-27")
    print("Total Questions: 150 | Time: 3 Hours (simulated)")
    print("="*60 + "\n")
    print("Instructions: For each question, type A, B, C, or D and press Enter.\n")
    
    user_answers = []
    score = 0
    
    for idx, q in enumerate(questions, start=1):
        print(f"Q{idx}. {q['text']}")
        for opt_letter, opt_text in zip(["A", "B", "C", "D"], q["options"]):
            print(f"   {opt_letter}. {opt_text}")
        
        while True:
            choice = input("Your answer: ").strip().upper()
            if choice in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please enter A, B, C, or D.")
        
        selected_idx = ord(choice) - ord('A')
        user_answers.append(selected_idx)
        if selected_idx == q["answer"]:
            score += 1
        print()  # blank line for readability
    
    # Show final result
    print("\n" + "="*60)
    print(f"TEST COMPLETED")
    print(f"Your Score: {score} / {len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")
    if percentage >= 60:
        print("Result: PASS")
    else:
        print("Result: FAIL")
    print("="*60)
    
    # Optionally show detailed answers
    show_details = input("\nShow detailed answer key? (y/n): ").strip().lower()
    if show_details == 'y':
        print("\nDetailed Answers:\n")
        for idx, q in enumerate(questions, start=1):
            correct_letter = chr(ord('A') + q["answer"])
            user_letter = chr(ord('A') + user_answers[idx-1])
            status = "✓" if user_answers[idx-1] == q["answer"] else "✗"
            print(f"Q{idx}. {status} Correct: {correct_letter}, Your: {user_letter}")

if __name__ == "__main__":
    run_test()
