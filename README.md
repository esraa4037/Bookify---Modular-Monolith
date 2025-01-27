# Bookify

Bookify is a backend system for a doctor appointment booking application. The system is designed for a specific single doctor and handles the logic behind managing
and booking appointments. The project is constructed in a modular monolith architecture style. In this project we don't care about authentication or authorization (all APIs are public). The main focus of this project is to apply different architecture patterns in the modules and make these modules to communicate with each other using (direct call & events)



### Business requirements

1. **Doctor Availability:**
   a.​ As a doctor, I want to be able to list my slots
   b.​ As a doctor, I want to be able to add new slots where a single time slot should have the following:
   i. Id: Guid
   ii.​ Time: Date → 22/02/2023 04:30 pm
   iii.​ IsReserved: bool
   iv.​ Cost: Decimal
2. **Appointment Booking:**
   a.​ As a Patient, I want to be able to view all doctors' available (only) slots
   b.​ As a Patient, I want to be able to book an appointment on a free slot where. An Appointment should have the following:
   i.​ Id: Guid
   ii.​ SlotId: Guid
   iii.​ PatientId: Guid
   iv.​ PatientName: string
   v.​ ReservedAt: Date
3. **Appointment Confirmation:**
   a.​ Once a patient schedules an appointment, the system should send a confirmation notification to the patient and the doctor
   b.​ The confirmation notification should include the appointment details, such as the patient's name, appointment time, and Doctor's name.
   c.​ For the sake of simplicity, the notification could be just a print message
4. **Doctor Appointment Management:**
   a.​ As a Doctor, I want to be able to view my upcoming appointments.
   b.​ As a Doctor, I want to be able to mark appointments as completed or cancel them if necessary.



### Architecture

**Modules:**
The system consists of four modules each with a different architecture as follows:
a.​ **Doctor Availability Module:** Traditional Layered Architecture
b.​ **Appointment Booking Module:** Clean architecture
c.​ **Appointment Confirmation Module:** Traditional Layered architecture
d.​ **Doctor Appointment Management:** Hexagonal Architecture

**Communication between modules:**
Modules could communicate with each other through an interface which named with 'facade' postfix and this can be occured just through the shared folders placed at each module. Some modules no one call them so its share folder is empty.



### Project setup

- Clone the repository and open the terminal from the root directory of the project

- Make a virtual environment
  ```
  python3 -m venv venv
  ```
- Activate the environment
  on linux:
  ```
  source venv/bin/activate
  ```
  on windows:
  ```
  venv\Scripts\activate
  ```
- Install packages in `requirements.txt` in the venv you created
  ```
  pip install -r requirements.txt
  ```
- Run the application
  ```
  python3 manage.py runserver
  ```
- Now, the application is running at at `http://127.0.0.1:8000/`
- You can route to `http://127.0.0.1:8000/swagger/` to open API documentation and interact with it
