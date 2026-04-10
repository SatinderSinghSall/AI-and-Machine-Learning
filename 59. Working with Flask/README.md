# AI / ML: Working with Flask

---

# 🚀 Flask Web Development Module

## 📘 Overview

This repository contains all the concepts, examples, and implementations covered in the **Flask module** as part of the **AI/ML Prime Batch program**. The module focuses on building web applications using the Flask framework, covering both foundational and intermediate concepts.

---

## 🎯 Learning Objectives

By completing this module, I have gained the ability to:

- Understand the fundamentals of the Flask framework
- Build dynamic web applications using Python
- Render HTML templates with Jinja2
- Handle user input via forms
- Work with query parameters and APIs
- Structure scalable Flask applications
- Implement message flashing and redirects
- Deploy Flask-based AI assistants

---

## 🧩 Topics Covered

### 1. Introduction to Flask

- What is Flask and why use it
- Setting up a Flask environment
- Creating a basic Flask application
- Understanding routes and request handling

---

### 2. Rendering Templates & Static Files

- Using `render_template()`
- Passing data to HTML templates
- Managing static assets (CSS, JS, images)
- Folder structure (`templates/`, `static/`)

---

### 3. Changing Default Structure

- Customizing project structure
- Modularizing Flask applications
- Best practices for maintainability

---

### 4. Handling Forms

- Capturing user input using HTML forms
- Handling `GET` and `POST` requests
- Accessing form data in Flask
- Basic validation concepts

---

### 5. Query Strings

- Using query parameters in URLs
- Accessing query strings via `request.args`
- Use cases in dynamic applications

---

### 6. APIs with JSON

- Returning JSON responses using `jsonify()`
- Building simple APIs
- Understanding REST basics

---

### 7. Jinja2 Templating

- Template syntax (`{{ }}`, `{% %}`)
- Conditional rendering
- Loops and template logic
- Dynamic content generation

---

### 8. Template Inheritance

- Using base templates
- Reusable layouts
- `extends` and `block` keywords

---

### 9. Message Flashing & Redirects

- Flash messages for user feedback
- Using `redirect()` and `url_for()`
- Managing sessions (basics)

---

### 10. Deploying AI Assistant (with Flask)

- Integrating AI/ML models into Flask apps
- Creating endpoints for AI interaction
- Deployment considerations

---

### 11. Additional Resources

- AI Assistant Code (PDF)
- JavaScript Resource (PDF)

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML5 / CSS3**
- **Jinja2**
- **JavaScript (basic integration)**
- **REST APIs (JSON)**

---

## 📁 Project Structure (Typical)

```
project/
│
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-project.git
cd flask-project
```

2. Create virtual environment:

```bash
python -m venv venv
```

3. Activate environment:

- Windows:

```bash
venv\Scripts\activate
```

- Mac/Linux:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
python app.py
```

6. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📌 Key Learnings

- Flask is lightweight yet powerful for web development
- Jinja2 enables dynamic rendering of web pages
- APIs and JSON handling are essential for modern applications
- Structuring projects properly improves scalability
- Flask can be extended to deploy AI-powered applications

---

## 📚 References

- Flask Official Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Jinja2 Documentation: [https://jinja.palletsprojects.com/](https://jinja.palletsprojects.com/)

---

## 👨‍💻 Author

**Satinder Singh Sall**
AI/ML Prime Batch Student

---

## 📄 License

This project is for academic and educational purposes.

---

# AI / ML: Flask

---

# 🚀 Flask Web Development Module

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Lightweight_Framework-black?logo=flask)
![Jinja2](https://img.shields.io/badge/Jinja2-Templating-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

## 📘 Overview

This repository documents my learning and implementation of **Flask Web Development** as part of the **AI/ML Prime Batch Program**.

It covers the complete journey from building a basic Flask app to deploying an **AI-powered assistant**, focusing on both **theoretical understanding** and **practical implementation**.

---

## 🎯 Learning Outcomes

- Build dynamic web apps using Flask
- Understand routing, templating, and request handling
- Work with forms, APIs, and JSON
- Apply Jinja2 templating for dynamic UI
- Structure scalable Flask applications
- Deploy AI-powered Flask applications

---

# 🧩 Module Breakdown

---

## 🔹 1. Introduction to Flask

![Image](https://images.openai.com/static-rsc-4/pVkaUkkMsx4nR-7KEx20uiEG67NUhYAdnH2WVEYW-v8X9MnP3nyP6CHLkv96pe8EdMVK4uv1Xvau4qnx1cxpAQVoMdUX9sKWVGYLbVGR6RcW0ffOGDt9BxMuILhGCk2LModcLhCjjXytO-HA7j-XOlfoX0T3hqjUG0deNsXUtFPyc2dni46RopH_LU6DmE78?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/M5MD6ObkG_-458TM5CoTxMV6-52ZJn9dUiVC-m4MmY-tOnfZlUvqKx3ovU1ZRK7mcxoIskP5bGj8gsWK1e_NxYVXrjTVp08vu9PobqhGKD6yRQg1tBGyM9Guw16dJroR-kASWEaU8iYoTgoQ4XVtKqKLTQq6H5z2GR379pGvOOujHOSmvsbcjIQfTUyhZGlK?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/dngDUnmChZ3HekBA9_-Pw-fOSW8V6vQZ76990E3PUZSVtvjbssuzFDzRwPfJPPhcUlgPc2swpySJikzG7n_TkEkEHbxBwUirHbMMoJRZlpwwQvJwLHApyeVRVopa_2KCI41YoTI_hlbGHh9YjI-hjmBZGXlwO6ofEJ_PzF6wE_16PnoervdZtr43L7EgnusT?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/W97bzKM4wHYMr3NZDqaGh0-WcICoTPDD3nCFGVJl0qSPlzfX9GUgK2FCk9eQ3su-HLF1p_Qq2uBhWoo6_eeVtS3kA2mJKQpnEXwNucMyrlmYIqoqYwReqVW4b_36NHAjMoWG0WTToJvenvq2S7teKKlpyApvvq1a356ar5vmbo3Hl-nEdeh1iU2bpTR9E7WZ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/bksYA5YXXMhXIAVH7xvGLhckeVLcCQZFQpQmEZCCfNKCsAYL1J0I0HnjiQTpKjZU0FPHWomaVmedYnGKyLF8oVyTDoK-fnrP7P91UG3OVhdkdIFKXOkWfTWGrxdbqagyIOxmx1SK1qtpxPzGpADlDXsVfBsc2iWNLMYKySLuVrM86K_uIDUu9vuI8ZtLRYS0?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/VRYXbeVW7rGKKP4H7Ujl4os1_VHwtZUODgT7wqDo194nXZVUdmLVy9Yt0anA1O_RSfEJwMdOIHuzFeLHaWUK3hCQaJN81h73Cs_yYezvqZbkL23mhRcTqBvzncvRKK0Hp2Vo0S3X7D3UmszKndvdOIfPzxZlbe-eXONRA-vmF1EArtKCmHLNWkn2lpx7ourT?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/XSk7Ats9PqZJMVPKaEJNLQEGMdBLqjR3uXdGcOXu-n7MMBU5pwUZ0FUW-thUoC38VmwYcW9GX-Q0RB1XUzjNGYhz9EGZiKtV5G6Rcd86xfykHK61ty1jZER4bXrPMBoiy1FQicNSpdFiP9mWT6bZqJ2hpx2vc0-pz3by_vOLfnF7mC9nnVpION7Ushm0Ksph?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/2W6Nwkijw1XreZF5osLTJZzsHUmme3nTuQVrPUy8PZ9yVIAJJiKfEnDYsnoOjCAUdAFqhcTWyhNg8XBkuM8JTENx9Q7bP5QL8q5LFXvMIxOR1WMn0rjZBmhxfaLcrnH3BlCpFJhaQsfSuslEDCZe3GkkVYc5xut-cu3QMuwoMsl3z_Av4DHX2NC22MvTdlsO?purpose=fullsize)

- Lightweight Python web framework
- Simple routing system
- Minimal setup for rapid development

### 💻 Example

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🔹 2. Templates & Static Files

![Image](https://images.openai.com/static-rsc-4/lDw4XDo2o1FAVamyc2E9fPC1MZTkXTbyn_BwA2dG19t64hYs-vnRYbDbDXqcHxVmwCuv_D5PSrlBB8jry76eHgrvrSIz1d9rqH2_Fph8OY0qOmumfYcz0jgWIcvBjD8Lx-54bzS22zEJzrdCIELocWY17wHxDhKPIN7JH7HqG9eZMiF7oYGPZ8IXOS1u8OvY?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/R-yZWhUcwNZRArQlksYdYkUwiMlzocEDmQ9IPwcyfGU8vXp3CN-LYUrMzkD-7PQ15bA8mFi_ao8Y6XeMduTwy-r6Rbedvtoh99OqKHh0OvU7PruEChlFHh16GjBK2sivMuGB3qHo26cjvJxIYext3gJjmCKUczCOcKKat-BCYr6DipjLWhZEM0ek7GejWjAg?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/djXVyp97LrZk0bKD7hJNZO62AukWFbqhSwTNew5Xpi4sUR2egggM0R9AqpV298_D-er6_f5ygN-VapJcml7665KLkjQht1QUNOnPyFPvsogFInLfYmmVrLpL8MvdU9Z4cSypZvLTI3gONkEskyCedfNs9O--HPQHlYOL6ghSoZxiKK50Hqb1EhTJp-R9GDTv?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Y-Tme6tGN0EmiOcMaO8Llq83MBRnyGpdrWf3P64BMrNqxCvxoEUkWoSAhgYIMBRcO2WhYfMkZdZF78iyv-_-h1dicEwhQmdWLkLzJtJsw0WslesjkC-Bkz8Wp7-L-4zkVu4K8zPOcc0bfwkh5-lo30EEKmdlT100t0BGlZLloTk3Vwo0m6kIXI5biulm8w-H?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/wW-H8-dTabDkJMe4eBlMHG6wSZ2uHdYK_u3dJBGH-rwBpOvuWH55A0o0Eu0x0SDsxZgxhXKuUoh1xt-0MuYmr64L4Wyr3FCoCaB9fiydgDD1gBRWYul7jGetOcS2dF_ngJBWgDop2MSgx1g8gHgIMFwynM7SnGlMbJq13KHSRytUH2bfl_fKEmOfHW2jnxb-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/1Vcf6nr0fv6PUIIC4jm5BiYmPQJBeBZVb85pMFqrRllVwOHCWjgCdtfWSnYPRVj0SMp_sbrM0O8kbNi_KmBLIh_PcsZxKB0mfghJMreXsIFw7bn5AZZS1bS0SFmxAEp4AbUHTrRQFeskbctM_YcOL711ahR43mElaq2YGxo2oLU6bJUQ3JSwePYjeJPRdvN1?purpose=fullsize)

- `render_template()` usage
- Passing dynamic data
- Managing static assets

### 💻 Example

```python
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html", name="Satinder")
```

---

## 🔹 3. Handling Forms

![Image](https://images.openai.com/static-rsc-4/kOtn5sXq6SkHMsJjM0OTDaJmVNfihvosPlTNytVThi5yrC96OXNaNetfBnyctWl4XLNR59ceB_zAfld-rNBMTC0Irdsci1Qre6rIO0pRarL8RlYzqdndm_QRqCbjxzGlEyqTX_vRdnnERBVhMF5E5CIrMq5O_qkOKQeyPb15TepuY28J3cz9XXxnglcG5rYx?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/PE5Y84t3pVN7Ll2FyTfkeWooCVrcM9pVukTOq5DjTVtFRfKZA2Plqb-llzPMt1vAm4Nsgr-CEkAb-tVHvfcvTr6TbrvqGOyI_hJRT7mHf-P7pDHpzUVZGneKZOQ_NJOw7igBnUt7cddIPdm7RUvJxi-HIDcs_whLC4kftfuDuVj8VUU2XZuoj9uUeAinS7Qy?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UDg0h8BSayd-8g8PbMdqTwC2i-7MpkRABwkAmu62x8I5BD-hKQjGgzodZuRCVZ7MR4W83XpH3HWZOWlzjMY_XUNu7mfbLSv_HErlUzELEyTEs5RcEad_RUFV6GPlHtqaTSTh_0M5ztTyGzx3Xwr4KIGExIS-kPiGaCQD1TJGpZgR-UZhjGCC2rUGgz-Ja9dz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/y_VuSoQO8-ATdZgOYcVws6huszUyNkV0McH6cLlO2vP50eFgwPxGxPbtor_reQ_kSh7szm1i8QPO_MiMWd4xbo5wKr9W3-R6Ldn2Z82IQ-EqFuLLUuiAnTAEIXpBjyfoZHWmUddMBHxnSMuqKTHfzMP8YR1F_GmgbnRYvmeeUHMy_20i1T_zOm1Z7evMr3OD?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ZSDs3O7k4tbecBV_SOeiEP8wAgSB3-Nv7sR9flWzro_HPz2bgMLI-JARDYgRPSQ7NziikpoK4_Phofkg3BqqZVwF3faW7k5BHYAsYPTuhYtErkT4brZhDgfODRcSC7t1BknFljfU83267Jl4OZWucbzS9EAx4V_97xiFvQguQ72FUBo7EuUXTNbi0hafm8iH?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/zf_Tzy3q33RN-oFBdorswWuLsTprtizOfriPX9B4bp98HjJlSO6IOVb_u92lMT_abqg_75b-2-WZhOXErzfZ8oXoCreLutkPs9CL1jXm9rGVwjTDpy6mBLe3XKvQVgbTu_cIqwzMrGXCa-SnfDBoneRGuk9PSDUzzppt1Y5qpQRhdFnOoZHidqQO8U9k0cec?purpose=fullsize)

- GET vs POST requests
- Form data processing

### 💻 Example

```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f"Hello {username}"
```

---

## 🔹 4. Query Strings

![Image](https://images.openai.com/static-rsc-4/x-Lpwxp3WfuxzXIZmC3v4kWNSauWKttH4dKuFQ8HDevOZkqQDIOdzJRpQa13YjxMVDqZXLCSDqK9zaG0691SBpSuT113Mvy3d3q2oW-wrCnWk1PmyZ3dHnJ3JflVqvAO4dNeIrDkBv296MpSAFBrO5S1Lgeu_T9hRD0DlTrbh__lxO9sLwYLtIXzsnT5yuma?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/3SgFIfcXwKS2fU5PHHPrAjmzXut0dMpn0O80FZVu8bKNUeLRnmb1m1TFVu5qp9iC_n37_d7F7rgOJwK3LO60xJYRHrvZuVvS8NutISIlx4SGOyn5vG6OplhwAHVxlpObZ8jhY_TVe1TRoqGieSDpmvuyyd3OfDAJq64Dnxf_zLbGwkrNQRe6Yo0PcR_pBoE3?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/JSDw5coTX4Wuo2WJbEJXROLKzViMnu45uS-QC8dZXzbk1jeKdHFzcxd7oPfKKcjp83Va8kSkit6pzAMOi_ygPNpSEOdvvBeoY05iTRd4EfR8SPx0Kx_3751GJ1DM7qFOVrFZF3WohOuqwVZIaEybvEvqWl12_NXOEQaU5FKmsFRncQGeMmP_613foUPLzkNy?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/R1nI-38AAFX01icmjsrov7Wx3L1t72M6YvbdwwT7oizMBFAvDe-epEcxrRAFnhkZTiomSdD7jgcQDwxmBzbaH9ddFsKLWY8zPA1L59oylpUSlTDIq5AWwK9jA9Dn77pHND30nt19rw-sBI2xWt27tEZs34XcHbUX4PENwBiX2bgVBY8EiS7RoQs9FIOOvU-y?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UDg0h8BSayd-8g8PbMdqTwC2i-7MpkRABwkAmu62x8I5BD-hKQjGgzodZuRCVZ7MR4W83XpH3HWZOWlzjMY_XUNu7mfbLSv_HErlUzELEyTEs5RcEad_RUFV6GPlHtqaTSTh_0M5ztTyGzx3Xwr4KIGExIS-kPiGaCQD1TJGpZgR-UZhjGCC2rUGgz-Ja9dz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/5-x_fn9YzQbN5xroiRcz9euKjDjo4se8J5NacB_FPCFo4uJ-vgxk0pLbIwX05-td0U2rsrC_ANsewSGdCUhZutnNHZ8nsNw5g52PNsKVOztflaPRnAyInOjXNTmJNOu8o48StWCpEY_3ThV0YNwl0Yz00IA1FmJsnMaVnU_YP11gNfO1Ps4c3U5N-wsTU1gl?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/V5XzSafbiU0ieNedieZhr06mdfSrWQfYxUTNVlw4enjX2ebocLqSzb1NxSQe5hKNl-agCgkwXamYG9E58LpXeTnEsBa1agLChuz2HcywRPdKvj96_7qBQQmp26FhsjXk5fEO_gDBuDFii5VUMk0UafjJi7Zqyn0ZFbQBl8vox17HpQ0SV_XKO41mFy2fQuRi?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/5JLjsA5z3mtycokbaC3DRkB3f1DoHyQwqE_PMXMpBfX1Uyrz8aIA3MnetP-8CMPacqeci0Brn8kn91Odv_Ey1ZCTIRvbdf2Wh40nMfUUmZ59G0jeX8HL2bty2h9jhywVzbXkWU16Vpr6WIvR_PrzQhU9cqM_iaU93Fe8TBToyvRr1PKYFK5CpK14OraYukVp?purpose=fullsize)

- Handling URL parameters

```python
@app.route('/greet')
def greet():
    name = request.args.get('name')
    return f"Hello {name}"
```

---

## 🔹 5. APIs with JSON

![Image](https://images.openai.com/static-rsc-4/NnduoC1M2LktO-KMJHKXvs-MGaerYcJBYEJGQX1Ed3qQ2j0kv5SiXCrLomhqsrhL30U2PboRdrwjho8kA-LrB3_UoClLHKHbNbxdggDhX8kNTSTqCyavJaEJIPXX6p8-4LDfGKsKzgRG3KpK5riK7if7RDMHa1e8QQomxhEya20l8JiJwZbBVN7p96xB2TIh?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/2MSalglDH4x68IwoTHS-cD_Cq9RZp5VuFTA3MlKQwzYT7Hab1r3qpkCG0pyMYK96e-2ZHyZpTQIc1_u42yKxPOy2e-hdodrBcSMuS2yO1cGThPHEeZx1-1Uq2ziBeq7DqVCgQ09KTYLuzsAwookxOdq_NFXHjuql8QjEQ8VSKvyVxZCi3OcCskuBNhwtWTBH?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/V5XzSafbiU0ieNedieZhr06mdfSrWQfYxUTNVlw4enjX2ebocLqSzb1NxSQe5hKNl-agCgkwXamYG9E58LpXeTnEsBa1agLChuz2HcywRPdKvj96_7qBQQmp26FhsjXk5fEO_gDBuDFii5VUMk0UafjJi7Zqyn0ZFbQBl8vox17HpQ0SV_XKO41mFy2fQuRi?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/T5vqIYrXh34e_Q6gi1T_6Is8jHWH2MdC2sVaUk1e9zl6_LiZKilS9Y6AHw_cMf1h-oUjK2nKLxfBh5ZuzH3XHOm9i1nHpYP0fiqqe_0zBo9mS3fcK9cNfxt_5mNJtDoSidhlu3S8PmnmglwchjncWhhwFRD_n3uBVOlzOkrD6NUT4tIMepUWxXV4G-SEHKWm?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ujpYfIA1H9J6VbgKGjVgJv8Q9JndekGM_oovkAEbDj5rVe0JuWkDm3uHBn4Mykir80GfNXfCdtc7AiLomkHVdGnUDRqODp4R6xbEXX3Ftkm7BDWXOBfVJH5BQ_X-5U9jY5i7eGMe6A-O_KDuPs5_BcmKofuxIOjEfvfI_4aba3E_wLB1wyLlh8F9jHeczdZT?purpose=fullsize)

- Building REST APIs
- Returning JSON responses

```python
from flask import jsonify

@app.route('/api/data')
def data():
    return jsonify({"name": "Satinder", "role": "Student"})
```

---

## 🔹 6. Jinja2 Templating

![Image](https://images.openai.com/static-rsc-4/tJMU5pbZeOK2m9riwdgnUyQm7Lx4Pz8XprqdbdhKXDHuoddheitMPlsL_wMxB9DvD_WpTyJ0hC4Ift-9xNGEb-MSjg7CvZ0kIMEfgmb9iGjDzfmp03lEcYr4DoVlQ0C-QQ7f5MPKh7HQASbbuNIbbgRegoUlUdi5L6OZ02CpFn3rMftfLPRJm0ntJUh5hgBi?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/2JzvhKJSScEv38f9LjYTmmGK5FaBPzYZY5PwSt2Ez7fT6Vl7zLdIRc82iiqD7nPIbLqHgIIwn0xfqKcMQOwR_MrFJsSmb36MEY970uMTbrVXmGtrLyZSWYDYESikJl2v1dM4oTg71dnKmSMAxSywqEou7ARN4C9JXCJlSl2CZYSPAJxzLq_f8M0SrvdO1n4X?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ovgtPXQQMbm5LN0a1mmPJ-DeIHfcRYD2PRgTTm0rYx8cpKcDLVDI6RApt7V29Q_X7L4INFyrCXkp7Y1Xiigh7eMKkX7RAGzrd128g0wuzMejjm_aacxdueu2kES3KXg9L8zUyFtcAOhI-7RkUMe9QBUJQ4PXlXgF1wNHAk77nYaRxcX0pwplKkfWkTR-l4qa?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/okmT1Qp-IEdCLMRWI8cyDfNgJ5nC2PVk8Nj9NP-14k74KKIzArg6FaNf23W8tb0b7zuzNO9-hYQuAz6m5sYUIPUf2eqAr-dKQFxH8ixR22otfEW0zs3YGuTsvSHRPgSqjMCOcCOsEKnnxgWw9-fdiVfA5jo25JjnFHaa3f6cv7hg-KD0et-x95sJqFhvzvdC?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/3s64x-fTMQjZJ3xsOfd2XV5dwzmBUmHAceanYd6mMG9oe48DekHKq8D5FDPBHqdHEgTAymytrWL0rDoex6w909Mabo_q5BgaNlMEIUiQcMoFCtEJOiqVYVY6tqcJXzheHA_xUJ3UmiCnFv5cULCWqGpxxF8h_SFSpPWR1x600KwFDGlkHdJtU2HtL9ij_WO2?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/TZEXFfC3JdBqUMXxYHsz4K4LD2oL-npjBVCdVNtqWnwqWC1PXxLohYu1Wo5iV2nUY3e0oxGV6duQkpW3kcZtU4fmt2GdJqWBfhdBj-1wYi3GQnq3pqAEK0BUcRw1m0BCqUD09tpDjM3fwoBNHQG8IcCEMhwtpTql2RrfE3CPyYjdy_muz_9Uubs4ISxv8Hf7?purpose=fullsize)

- Template logic (`{{ }}`, `{% %}`)
- Loops and conditions

```html
{% for item in items %}
<p>{{ item }}</p>
{% endfor %}
```

---

## 🔹 7. Template Inheritance

![Image](https://images.openai.com/static-rsc-4/H5ZbFAw4Z5MdJvl2rRvgkR0t0n6PDWqU11ZKo-MdiZnDq9rd_fu5XM7jdF2SD2hZqnpy077BKblh8SG06LEjaCSR1LWb5qI-Z-GT0howQOvF8OEmsPc9wHZgAFTkT2JODxje4oSKtWsS8iC6SFjN99OpVgw8RLymeYhk8D_L6rz1CaDBSVaFLnFat3YVqBKK?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Afe3xPfoBYw9RYJ7HFGG8jtc5ZhzcC8WIvajycLW4_xNuBw5o3YcGRmd91nTS9AAddQcPORBKATKJ_R6wF2Q-0hb_ThkjsRk9DhbEXi2wbhJTx39VBWhAyjJs4mC-NS4wfMCO4D2mbkOzUI19oZNJHlk2z5QdFcWMlsi-TDtWzzY798asWBlEFl8yCErUjzz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/6Dkw6SpqFC9urPkG-gQo1LW15O7cwtBv4LdFq5DZP-5VmxNTO5BvhMbyh8cwp-Nt2qREIUhwHhrKTHXkXZUQjYzKZcMgob9MVzYRuPcDyknWtetS90kzvwak4gRFkYMT2aAfPC1u1gMKuAsPm4ni8laHOPOsUFDwL9IB7hFUigGMrIp-63HC1_I6s8MCjPzr?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/djXVyp97LrZk0bKD7hJNZO62AukWFbqhSwTNew5Xpi4sUR2egggM0R9AqpV298_D-er6_f5ygN-VapJcml7665KLkjQht1QUNOnPyFPvsogFInLfYmmVrLpL8MvdU9Z4cSypZvLTI3gONkEskyCedfNs9O--HPQHlYOL6ghSoZxiKK50Hqb1EhTJp-R9GDTv?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/TkUQQ2Zm9k9nhcdlyi4MR0RrYg26L3NvWyhWKqAwX7F-YVTiLc1kOd2ezzmgxZ4QMeOtTrR_KggIMRW_W33j-kgOAiIS2pUmYtMdFC8-rDIwDVEhQtbV_h8526wfEWvpgp4f6LPy5jwUQIcMTyqstkC24szlXaz6HpodUYDsS70KS5gZxYEiPBiLYF50RTgB?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/sX7QcnnOOgCNjmyKaZWX4Mjpk0y2XwLEWVpbP3Tg6Z8aZH0M-oBvKlvEsCln3rtnsa-BGlTGi4H53BwOWVicwjs8c_klp_sEdAhv3Q1n1tn2rMWPNZyNuMR6F-5mcpPPwFqGgGB-nlHns4k_EI7-JBY0hmjMYGdSk_Q2lJzS9e94teSSCdxQXwgzsr7XSZml?purpose=fullsize)

- Reusable layouts
- `extends` and `block`

```html
{% extends "base.html" %} {% block content %}
<h1>Home Page</h1>
{% endblock %}
```

---

## 🔹 8. Flash Messages & Redirects

![Image](https://images.openai.com/static-rsc-4/clM-bvSjE_Dd0U1xE-DLwdVCySq87T4qj8gUjdqs-74BpUJlKgFjr7ZjLLLKOnP0W1FW9bgSGUXS0ajn-xZ3H1OP1I0EppPtBzUr-lTBgPoSTujjqBbrQOVVqEK8RhuJADY6apyLyYPbXomEo2m7h9-kKI-922Z_oJ-LsdSMsgqmJi8Grahia-NcXCIOcIMz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/uaCL07H_RBdQuQihkMP7Wd6t6tY3sCC5trVWWe7rsGkriKulzUr2JLWK2nVX5v382hf20WNsNpf-CvlX6veNTSHjzmTuuQDX6fOq5DAQd8mvIxSFZqcVX9HmR_iOHKEF003jcsJDaJSs3RP1Coc2mKFsxUuO8dUx_Kt79WCbLJXbKryu9lMeu8q_Hs_zdQFv?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/x-Lpwxp3WfuxzXIZmC3v4kWNSauWKttH4dKuFQ8HDevOZkqQDIOdzJRpQa13YjxMVDqZXLCSDqK9zaG0691SBpSuT113Mvy3d3q2oW-wrCnWk1PmyZ3dHnJ3JflVqvAO4dNeIrDkBv296MpSAFBrO5S1Lgeu_T9hRD0DlTrbh__lxO9sLwYLtIXzsnT5yuma?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Bn9lqV8fI9VdoBEUpoLaF978L2QhqF9Z6z5ZpSA-wsSbHWm30MsW38NB-FDvy7699Oe8OI_Nv1SQveewKF-Mwkd4OyfpSgDadObov9Aet24ICkUY5zEsD_pbGlsRYKAV8XwIJROVe38OTlOvxEK4p6fsEnpSZZ0jRkFQ1WppZH9xfHE_APs1S6jVgzUjOBes?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/xdVtfh1mFso6FdwtXfoPJI6sOFGK8UNhgbLpSF9aQbkoachaqGbh79C2ESXswYTikuPdv5Tt6MTFQAtdP5q4TvtoC5Jt30f9oXlD4Bfjl2hB0N3Ri8yFRF__E_ErQd76MiS0UxOk4tmRhIvDF5W5bfsZqDgAGd2miRl67U-VG_iQcmMHUi513vUG8yIBL2FO?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/CIXljbd8msnRkHszxbOVsiXmcmt3fZt5bLeoKde6JMJwk9NM-yMyiAYYbzZ9-AY89-W1QtPGhiJbrzLNOyAcTpPDhHy_yOENNFzxGkN-t-hbuSM70BikY37S6VG_75kbNlUwL58yMVYtJ8pw5jWw5ZQVIa0zrlsDNzdPXcPrJxCS-21lmywxrQtl-gbLeG8i?purpose=fullsize)

- User feedback system
- Navigation control

```python
from flask import flash, redirect, url_for

flash("Login Successful!")
return redirect(url_for('home'))
```

---

## 🔹 9. AI Assistant Deployment

![Image](https://images.openai.com/static-rsc-4/aq-daE5C4mS0gd0mI2NBFNdMzEW3VRkwrFKZ3aqwXvbMGaZnCPo1Tv82GuKCLO6xlrUe157PZKGn3ZGjQPxHIoFqxCZ-hUrNW8Cit6OWEINvq1HAWzbiQv7R5vYfF7aApOvocRjcIKe3wQWXo_OsZe0ByqHnCnEwqTFpyTVusjxXuKl7ePtIyyhrygltq8vo?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/K1bmB-o-3_OyFOuZS4yT41--DVAI9Dp6MV5qAuekuABPeurY_J-3_rv5XPd-AHp4VQqkWoa24PQDzSGboq1SzAc4fCNtFvJ-qqbjhvw8DbycAsv1ZqUFiRyzaAh5HUs56wJ2EBmWyyprQ3gPMt6fw8cH5dwEv2JAmgEpEQLUdhAPAwOtk5Z10mS2kkhXH9gx?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/GkNOlwK-ZZ39VvqBIUWG33IuG5UuEUABNOH61OfRD82qcY16PoeiGSbkGhrdQsEYOOyz_ouIFgG6FhfUcbFdA3IFGbTDtUESap4MVi_dxVbP1VkfGUmm2y1zihfSQ9-7ypYZUa90F4REwfJr9mo6jAJdjlfzDl6XQbIz5_SFFBGz-RuPyv7LEMlWe20xgvpk?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/8_XCpaUK1NwcnzQrVus95uAOOvNXpNkOoCc6M_zU98w4c-mYri4oyGcKghgoMHZ5WTlyQNEiv14qxlmo79oOHHp7prVQrICm7Zfw_OGNelEC11o9IFhPjFEyZiLg5mZCzhcAc5exKxG9jUUBPEexA_Ho6LZmPgQ87m_c1ZLkdQuE_2zwZbNjX-lZFH1qxvJf?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/NnduoC1M2LktO-KMJHKXvs-MGaerYcJBYEJGQX1Ed3qQ2j0kv5SiXCrLomhqsrhL30U2PboRdrwjho8kA-LrB3_UoClLHKHbNbxdggDhX8kNTSTqCyavJaEJIPXX6p8-4LDfGKsKzgRG3KpK5riK7if7RDMHa1e8QQomxhEya20l8JiJwZbBVN7p96xB2TIh?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/pVkaUkkMsx4nR-7KEx20uiEG67NUhYAdnH2WVEYW-v8X9MnP3nyP6CHLkv96pe8EdMVK4uv1Xvau4qnx1cxpAQVoMdUX9sKWVGYLbVGR6RcW0ffOGDt9BxMuILhGCk2LModcLhCjjXytO-HA7j-XOlfoX0T3hqjUG0deNsXUtFPyc2dni46RopH_LU6DmE78?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/BJxHJ5QWdCyLL1PtSy2u2vk87JNKwnRIG0TYSFfqXfQITJcaQi48AyzGtMKHCEyfsKzNM75nitlU2oWtQDfJYTkbCqAGXWzCb0PngGjTJq94qxP1-8vFVI93PhtQQWYIKXKOdDsmg65kkNgFnZKBedBAYsQZNQuDqQXQrz-4Co_kuSKk8uqw9zAIFcgspfXM?purpose=fullsize)

- Integrating AI/ML models
- Creating intelligent endpoints
- Deployment workflow

---

# 🛠️ Tech Stack

- **Python**
- **Flask**
- **Jinja2**
- **HTML/CSS**
- **JavaScript**
- **REST APIs**

---

# 📁 Project Structure

```bash
project/
│
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│
├── static/
│   ├── css/
│   ├── js/
│
├── requirements.txt
└── README.md
```

---

# ▶️ Setup & Execution

```bash
git clone https://github.com/your-username/flask-project.git
cd flask-project
```

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

```bash
pip install -r requirements.txt
python app.py
```

🌐 Open: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

# 📌 Key Highlights

✔ Hands-on Flask development
✔ API creation using JSON
✔ Dynamic UI using Jinja2
✔ Clean project structuring
✔ AI integration capability

---

# 👨‍💻 Author

**Satinder Singh Sall**
AI/ML Prime Batch

---

# 📄 License

This project is intended for **academic and educational purposes only**.

---
