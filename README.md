# Resume-Project-Django
#### https://digulohar.pythonanywhere.com/ (This site will be disabled on Monday 25 November 2024)
## Overview

This is a Django project showcasing a portfolio website. It includes features such as a profile section, navigation links, and dynamic content pages. The project uses a custom CSS file for styling and includes images and navigation links to various sections like Home, Certificates, Projects, Services, Skills, and Contact.

## Project Structure

- `core/css/core.css`: Custom CSS file for styling the project.
- `core/images/20131044.jpg`: Profile image used in the project.
- `core/templates/`: Directory containing Django templates.

## Setup

### Prerequisites

- Python 3.10 or later
- Django 4.0 or later

### Installation
Clone the repository:
   git clone https://github.com/yourusername/your-repository.git

# Home Page
![image](https://github.com/user-attachments/assets/e07148b6-7b8a-4948-8b32-416b83fe721b)

## Overview

The home page of this Django project provides a brief introduction to the developer, showcasing their profile image, a personal introduction, and a summary of their skills and achievements.

## Template Details

This home page template extends `core/base.html` and includes the following key sections:

- **Profile Image**: Displays a profile image centered at the top of the page.

- **Introduction**: 
  - **Greeting**: A welcoming message with a personal touch.
  - **Personal Details**: 
    - **Name**: Digvijay Lohar
    - **Education**: B.Tech in engineering
    - **Skills**: Python, C, C++, Java, HTML, CSS, JavaScript, jQuery
    - **Experience**: Hands-on experience in web and Android development.
  - **Career Objective**: Seeking a challenging role to contribute to an organization's growth while staying updated with IT trends.
  - **Projects**: Details about various projects like Voting System, PDF security, RFID-based Door-lock system, etc.
  - **Certifications**: Python for Data Science from NPTEL, and achievements from HackerRank and Great Learning.

- **Call to Action**:
  - **Hire Me**: A button linking to the resume page.
  - **Contact**: A button linking to the contact page.

## Usage

This page is designed to provide a comprehensive overview of the developer's professional background and to serve as an entry point for potential employers or collaborators. It is styled using the `core.css` file and utilizes Django's static file handling and URL routing features.

## Styling and Assets

- **CSS**: The page uses styles defined in `core/css/core.css`.
- **Images**: The profile image is loaded from `core/images/20131044.jpg`.

## File Location

The template file can be found at: https://digulohar.pythonanywhere.com/
# Certificates Page
![image](https://github.com/user-attachments/assets/be1201f9-215a-4024-8bd2-ad45879eb978)

## Overview

The Certificates page showcases various certifications that the developer has achieved. The page is designed to be visually appealing with a grid layout for displaying certificate images.

## Template Details

This page extends `core/base.html` and includes the following sections:

- **Header**: 
  - Displays the page title "CERTIFICATES" in a highlighted color with a bottom border.

- **Certificate Sections**:
  - The certificates are displayed in a responsive grid layout using Bootstrap's grid system.
  - Each certificate is presented with a heading and an image.

### Certificates Displayed

1. **NPTEL**:
   - **Image**: `nptel.png`
   - **Description**: Certificate from NPTEL.

2. **Infosys**:
   - **Image**: `c1.png`
   - **Description**: Certificate from Infosys.

3. **Google Cloud**:
   - **Image**: `googlecloud.png`
   - **Description**: Certificate from Google Cloud.

4. **Infosys 3**:
   - **Image**: `c1.png`
   - **Description**: Another certificate from Infosys.

5. **Crash Course**:
   - **Image**: `CrashCourse.png`
   - **Description**: Certificate for completing a Crash Course.

6. **HackerRank**:
   - **Image**: `HackerRank.png`
   - **Description**: Certificate from HackerRank.

## Styling and Assets

- **CSS**: The page uses the base styles from `core/base.html`.
- **Images**: The certificates are loaded from the `core/images/` directory using Django's static file handling.

## File Location

The template file can be found at: https://digulohar.pythonanywhere.com/edu/certificate/
# Projects Page
![image](https://github.com/user-attachments/assets/7f5415da-ee2e-416c-bc1a-f474b492665f)

## Overview

The Projects page highlights various projects developed by the developer. It features a grid layout to display project details along with their images and links to the respective GitHub repositories.

## Template Details

This page extends `core/base.html` and includes the following sections:

- **Header**:
  - Displays the page title "PROJECTS" in a highlighted color with a bottom border.

- **Project Sections**:
  - Each project is displayed in a responsive grid layout using Bootstrap's grid system.
  - Each project includes a heading, an image, and a link to the project's GitHub repository.

### Projects Displayed

1. **Cloud-based Skin Disease Detection Using Machine Learning**:
   - **Image**: `projectskin.png`
   - **Description**: A project focused on detecting skin diseases using machine learning techniques.
   - **GitHub Link**: [View Project](https://github.com/DigvijayLohar/Cloud-based-skin-disease-detection-using-machine-learnig.git)

2. **Image Uploader Using Django**:
   - **Image**: `ProjectimgUploader.png`
   - **Description**: A Django-based application for uploading images.
   - **GitHub Link**: [View Project](https://github.com/DigvijayLohar/Image-Uploader-Django.git)

3. **Automating Bank Check Extraction from Scanned PDFs**:
   - **Image**: `projectAutoCheck.png`
   - **Description**: A tool for automating the extraction of bank check information from scanned PDFs.
   - **GitHub Link**: [View Project](https://github.com/Springboard-Internship-2024/Automating-Bank-Check-Extraction-from-Scanned-PDFs_May_2024.git)

## Styling and Assets

- **CSS**: The page uses the base styles from `core/base.html`.
- **Images**: Project images are loaded from the `core/images/` directory using Django's static file handling.

## File Location

The template file can be found at: https://digulohar.pythonanywhere.com/edu/projects/
# Services Page
![image](https://github.com/user-attachments/assets/f9025036-68ed-43fc-bf12-b57c1eba12e1)

## Overview

The Services page highlights the various services offered, displayed in a visually appealing layout with icons and descriptions.

## Template Details

This page extends `core/base.html` and includes the following sections:

- **Header**:
  - Displays the page title "SERVICES" with a highlighted color and a bottom border.

- **Services Sections**:
  - Organized in a responsive grid layout using Bootstrap's grid system.
  - Each service includes an icon, a heading, and a brief description.

### Services Displayed

1. **SEO**:
   - **Icon**: Search Dollar Icon (`fa-search-dollar`)
   - **Description**: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. laboriosam cum?"

2. **Web Design**:
   - **Icon**: Palette Icon (`fa-palette`)
   - **Description**: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. laboriosam cum?"

3. **Web Development**:
   - **Icon**: Code Icon (`fa-code`)
   - **Description**: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. laboriosam cum?"

4. **Android**:
   - **Icon**: Android Icon (`fa-android`)
   - **Description**: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. laboriosam cum?"

5. **iOS**:
   - **Icon**: Apple Icon (`fa-apple`)
   - **Description**: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. laboriosam cum?"

6. **Advertising**:
   - **Icon**: Add Icon (`fa-add`)
   - **Description**: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. laboriosam cum?"

7. **Logo Design**:
   - **Icon**: Pencil Icon (`fa-pencil`)
   - **Description**: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. laboriosam cum?"

8. **Hosting**:
   - **Icon**: Database Icon (`fa-database`)
   - **Description**: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. laboriosam cum?"

9. **Support**:
   - **Icon**: Headset Icon (`fa-headset`)
   - **Description**: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. laboriosam cum?"

## Styling and Assets

- **CSS**: The page uses the base styles from `core/base.html`.
- **Icons**: FontAwesome icons are used for representing services. Ensure that FontAwesome is included in your project.

## File Location

The template file can be found at: https://digulohar.pythonanywhere.com/serv/services/
# Skills Page
![image](https://github.com/user-attachments/assets/0900e746-293f-45ab-a51c-2d0262015e1d)

## Overview

The Skills page showcases the user's proficiency in various technical skills using progress bars to visually represent skill levels.

## Template Details

This page extends `core/base.html` and includes sections for different skills with associated progress bars indicating the level of proficiency.

### Skills Displayed

1. **HTML/CSS**:
   - **Proficiency**: 100%
   - **Progress Bar**: Red background indicating full proficiency.

2. **JavaScript**:
   - **Proficiency**: 95%
   - **Progress Bar**: Animated striped background indicating high proficiency.

3. **Python**:
   - **Proficiency**: 85%
   - **Progress Bar**: Blue background indicating strong proficiency.

4. **C**:
   - **Proficiency**: 95%
   - **Progress Bar**: Yellow background indicating high proficiency.

5. **CPP**:
   - **Proficiency**: 100%
   - **Progress Bar**: Red background indicating full proficiency.

6. **Machine Learning**:
   - **Proficiency**: 95%
   - **Progress Bar**: Animated striped background indicating high proficiency.

7. **Django**:
   - **Proficiency**: 100%
   - **Progress Bar**: Blue background indicating full proficiency.

8. **SQL**:
   - **Proficiency**: 95%
   - **Progress Bar**: Yellow background indicating high proficiency.

### Styling and Assets

- **CSS**: Uses Bootstrap's progress bar component with different colors and animation effects for a dynamic presentation.
- **Colors**:
  - Red for HTML/CSS and CPP
  - Blue for Python and Django
  - Yellow for C and SQL
  - Green for Machine Learning
- **Progress Bars**: Some progress bars are animated and striped for visual effect.

## File Location

The template file can be found at: https://digulohar.pythonanywhere.com/edu/skill/
# Contact Us Page
![image](https://github.com/user-attachments/assets/7c7972f1-2cf9-4755-b431-c133e5c09abf)
## Overview

The Contact Us page provides a form for users to reach out with questions or messages. It also includes contact details and social media links for further communication.

## Template Details

This page extends `core/base.html` and includes:

- A contact form for user inquiries.
- Contact information section with address, phone number, and email.
- Social media links for additional connectivity.

### Contact Form

- **Fields**:
  - **Your Name**: Text input for the user's name.
  - **Your Email**: Email input for the user's email address (required).
  - **Your Subject**: Text input for the subject of the message.
  - **Your Message**: Textarea for the user's message (required).
- **Button**: Submit button styled with a warning color (`btn-warning`).

### Contact Information

- **Address**: Karad, Maharastra, India
- **Phone**: 7277751007
- **Email**: digvijaylohar007@gmail.com

### Social Media Links

- [LinkedIn](https://www.linkedin.com/in/digvijay-lohar-169230244)
- [Facebook](#) (Placeholder link)
- [Instagram](#) (Placeholder link)
- [WhatsApp](#) (Placeholder link)

### Styling and Layout

- **Container**: Uses Bootstrap's container and row classes for layout.
- **Form**: Styled with `bg-dark`, `rounded`, and `shadow-lg` for a modern look.
- **Icons**: Font Awesome icons used for contact details and social media links.

## File Location

The template file can be found at: https://digulohar.pythonanywhere.com/contact/
