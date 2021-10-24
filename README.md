# ThaiRepose
[![Build Status](https://app.travis-ci.com/ThaiRepose/thairepose.svg?branch=main)](https://app.travis-ci.com/ThaiRepose/thairepose)    
**ThaiRepose** website is a web application that helps to find areas that users want to travel and it can help people to make decisions for making trips. People who don't even have any experience planning a trip before, it can help them to easily plan a trip. ThaiRepose.com will be a community for people who love to travel.

## Project Documents
- [Project Proposal](https://docs.google.com/document/d/1mOMiqBmQl6vW7RYVQD6Gk-mEcFnmdsmku2gpTglZRmE/edit?usp=sharing)

## Getting Started
### Requirements
|Name  | Recommended version(s)|   
|------|-----------------------|
|Python | 3.7 or higher |
|Django | 2.2 or higher |

### Install Packages
1. Clone this project repository to your machine.

    ```
    git clone https://github.com/ThaiRepose/thairepose.git
    ```
2. Get into the directory of this repository.

    ```
    cd thairepose
    ```
3. Create a virtual environment.

    ```
    python -m venv venv
    ```
4. Activate the virtual environment.

    - for Mac OS / Linux.   
    ```
    source venv/bin/activate
    ```
    - for Windows.   
    ```
    venv\Scripts\activate
    ```
5. Install all required packages.

    ```
    pip install -r requirements.txt
    ```
6. Create `.env` file in the same level as manage.py and write down:

    ```
    DEBUG=True
    SECRET_KEY=Your-Secret-Key
    HOSTS=localhost,127.0.0.1
    EMAIL_FROM_USER = email-for-send-verification-form 
    EMAIL_HOST_PASSWORD = email-password
    ```
    (If you don't use gmail. Please change EMAIL_PORT and EMAIL_HOST in setting)
7. Install TailwindCSS framework.

    ```
    python manage.py tailwind install
    ```
8. Build TailwindCSS frontend framework the get GUI.

    ```
    python manage.py tailwind build
    ```
9. Run this command to migrate the database.

    ```
    python manage.py migrate
    ```
10. Start running the server by this command.
    ```
    python manage.py runserver
    ```

## Team Members
| Name | Github  |
|------|:-------:|
| Tawan Boonma | [☕️ tboonma](https://github.com/tboonma) |
| Tanin Pewluangsawat | [💤 TaninDean](https://github.com/TaninDean) |
| Vitvara Varavithya | [💦 vitvara](https://github.com/vitvara) |
| Nabhan Suwanachote | [ ☔ nabhan-au](https://github.com/nabhan-au) |
