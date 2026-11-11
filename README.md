# Humanitarian Nutrition Data Quality Control (MUAC Validation)

## Project Overview
In emergency nutrition programs (such as OTP/TSFP), accurate classification of acute malnutrition is critical for timely treatment and lifesaving interventions. Human data entry errors can misclassify **Severe Acute Malnutrition (SAM)** as **Moderate Acute Malnutrition (MAM)** or **Normal**, leading to delayed medical care.

This project provides an automated Python pipeline using **Pandas** to inspect, filter, and correct classification errors based on **Mid-Upper Arm Circumference (MUAC)** measurements, ensuring full compliance with international **Sphere Standards**.

---

## Features & Standard Operating Logic
- **Automated Validation:** Scans screening records for children with `MUAC < 11.5 cm`.
- **Misclassification Correction:** Automatically updates incorrect statuses (`Normal` or `MAM`) to `SAM`.
- **High Performance:** Uses optimized vectorized operations (`.loc`) instead of slow iterations to process large-scale camp survey datasets efficiently.

---

## Tech Stack & Standards
- **Language:** Python 3.x
- **Libraries:** `pandas`, `numpy`
- **Humanitarian Standard:** Sphere Handbook (Nutrition & Food Security Guidelines)

---

## How to Run
```bash
# Clone the repository
git clone [https://github.com/S664470/sam-mam-data-validator.git]                                           

# Run the script
python clean_muac_data.py
