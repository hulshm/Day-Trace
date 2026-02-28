# DayTrace for Omi AI

DayTrace is an automated personal chronicler designed for the Omi AI wearable. It transforms ambient daily audio and location data into a structured, searchable history.

## 🌟 Overview
DayTrace solves the problem of "forgotten details" by acting as a passive digital diary. Whether you are managing business consulting projects or overseeing facilities, DayTrace ensures every commitment and location visit is logged without manual effort.

## 🚀 Key Features
* **Ambient Logging:** Continuously parses audio to identify key events and conversations.
* **Geospatial Tracking:** Tags interactions with specific locations (e.g., Home, Office, Client Sites).
* **Automated Summarization:** Generates a comprehensive "Daily Activity Report" every night at 8:00 PM.
* **Action Item Extraction:** Automatically identifies tasks and follow-ups mentioned during the day.

## 🛠️ Technical Configuration
This app utilizes Omi's webhook system to process the following notification scopes:
* **User Name & Facts:** For personalized context in summaries.
* **User Conversations:** To transcribe and analyze daily interactions.
* **User Chat:** To allow users to query their historical logs.

## 🔒 Privacy
DayTrace is built with privacy in mind. Data is processed to create the daily log and is handled according to Omi’s security standards.

## 📄 License
This project is licensed under the MIT License.
