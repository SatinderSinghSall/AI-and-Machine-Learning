# AI / ML: Agentic AI

---

# 🚀 Agentic AI Systems — End-to-End Implementation with Agno

> **Production-Ready Multi-Agent AI Systems | Prime AI/ML Batch**

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![LLM](https://img.shields.io/badge/LLM-Groq%20%7C%20OpenAI-green)
![Framework](https://img.shields.io/badge/Framework-Agno-orange)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

## 🧠 Overview

This repository presents a **complete implementation of Agentic AI systems**, built during the _Agentic AI module_ of the Prime AI/ML program.

Unlike traditional LLM applications, this project focuses on **autonomous agents that can:**

- Use tools
- Maintain memory
- Collaborate with other agents
- Analyze real-world data
- Be deployed as interactive applications

---

## 🎓 Topics Covered (From Course Module)

Based on your coursework progression:

- Introduction to Agentic AI
- Agentic AI vs Traditional AI Agents
- Agent Frameworks & Platforms
- Core Concepts of Agentic AI
- Building First Agent (Agno)
- Finance Agent
- Multi-Agent Teams
- Agents with Memory
- YouTube Analyzer Agent
- Deployment with Streamlit

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[User Input] --> B[Agent System]
    B --> C{Decision Layer}

    C --> D[Tool Usage]
    C --> E[Memory Access]
    C --> F[Multi-Agent Routing]

    D --> G[DuckDuckGo / YFinance / YouTube]
    E --> H[SQLite Memory DB]
    F --> I[Team of Agents]

    G --> J[LLM Processing]
    H --> J
    I --> J

    J --> K[Structured Response]
```

---

## ⚙️ Tech Stack

| Category  | Technologies                  |
| --------- | ----------------------------- |
| Language  | Python                        |
| Framework | Agno                          |
| Models    | Groq (Qwen 32B), OpenAI       |
| Tools     | DuckDuckGo, YFinance, YouTube |
| Memory    | SQLite                        |
| UI        | Streamlit                     |
| Env Mgmt  | dotenv                        |

---

## 📂 Project Structure

```bash
.
├── agent.py                # Tool-enabled travel agent
├── finance.py              # Financial analysis agent
├── memory.py               # Persistent memory agent
├── team.py                 # Multi-agent collaboration system
├── youtube_analyzer.py     # YouTube analysis agent
├── ui.py                   # Streamlit frontend
├── README.md               # Documentation
```

---

## 🔍 Core Implementations

---

### 🧭 1. Tool-Enabled Agent (Travel Assistant)

![Image](https://images.openai.com/static-rsc-4/YCIxZkNPppgL--fvyDdaIuFZ4V7RfIQU9SXHQVKihRO9Rhd7Ay23wPUEX75OBzMod_t5gWzmOO4nWEjoY-AtjhrNie5SrGlhO9YKf1meoXWnsiURPRSU9rQ6Su2qTNJscz_BBwY07iAddVQqSdLQciBlLpeExlZ8o7qZTTtW7ZZUDnac4ZqYJ5lYJDMbH2Ql?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/l-m2S8dP7dGzP_FNb0lx5MR-s1n_C9DVWbl2a4YgQbQ9A4f40nWO7hye6rATzm0lmlFpcB-7TllwcTo_5MdXOqhB_sYMOkQks33g2qyxYQYoyAS0uDEP5uCUKr_rBxg7AGu9TfMgaDvva_GfKVjm4FZTaSri2muE8LdQ6QOJdeWVTbVcW6Fs895GhfwlYwC5?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/lSQ05jD3LPy4UfQ28xZebB6rf8WVcka3UJirEuArVdF9ku-zFVO-WhJO8oTAQIsIFNomybmDL1WfWdQUlSU2-cLYnsx4YyDDAFu8_vILYVIx8Yb6FjHQfMzLF4daHNw3RG-qp3XvsVwHRrQFJgnO7gPh6k3k-Jw4CElj6JcGxq0s_boOnX0ZViG-L1j8Jo5r?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/QORqUWH8f-JQ55DHOlARqIg3O4YQh4msa4_R8tGCRP_YkVuAaw-cT6KIh9ALSKHNCAfwFbi-EDdTcI0ljr1F0CWB5z8zQOkHT-yWkEfIiiH-yO49b537I3r8Vna9CK39ssu8iLVh6f51n8RSUblgrlcur-fM6E4BEd4MyS7hzzOTBUXlYrbrYaQG-BFb6sBU?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Aq8kOrwL-dnmGPrEfA-mYQVrReAgZhYerv_ab3xPW4yNYxvM7jcn8SfL_Fd9CDg4mmisShLs-cMrd3nRDfl6y-a-iNo3pYHypA1Hz_0C1aehwgu7Gv70dppbtWgiT9ZsX6yLO0awk508QLCYtr3cultzkfu0V1zt_7j5JO1coAR9PZYyqN_ICR4kWZdduvDC?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UGACKmJp420aMv7seEURsmq5pb8L6hLW6B0LFZNFpEMEGjNkWzaQgr7Dyq2RyvB-9SCTgvUYcm3MSaKyI7yJ-CCwrqKXfizFycLNPbJldNRupriEkryFODlIsowcCjnExiXX-pq-BZfP3BZITxwOZuB7nhalvmjyHuRLHien2Xksxy_PkxOWuI4znYsY1tjW?purpose=fullsize)

- Uses **DuckDuckGo tools**
- Adds **real-time context (date/time)**
- Performs **web-assisted reasoning**

```python
Agent(
    model=Groq(id="qwen/qwen3-32b"),
    tools=[DuckDuckGoTools()],
    instructions="You are a helpful and expert travel agent."
)
```

📄 Source:

---

### 📊 2. Finance Agent (Real-Time Market Analysis)

![Image](https://images.openai.com/static-rsc-4/5ul_sYoGAOwTmfqsUGoYoY7uCuYJa58pmdGwefdKfJiYd-bMKxjrU6qL-4VM62XZMITWH25Sij3vjimZcPs9b8oaO3fMT7qikSC0tBqW2luUrmYlbd5ejqjehi4OBdh0fe2ODkCdkXRmMzi3ewBuGY_0-HTPD9cJu_e_iCB_g1piyzKHzlSjPaBrZE-jd8AR?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/e-YgtcqKvsHh_dMt874nhcOZUFX-aL7Quw8d6XPZ1jX7MRXzDUk73l4P2YwNYMB2zfI5CWfW84gNv3lDefYd5iIFqpYl-FfmbXpXvucmUJC0nqylpg4OwIg0s8Wgb8l-Ph7qdBh3m-yB7Ax_sU14svzqDCr63wiQUDryK3h5cbVBACp-r0uOvxDivt7CEJaw?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/nvIfbWfzGO2Q_sS837uxAUuLEiYO42SloB2K25OCUPWoUJVmB7-3hXdV48mWa_vpxZGpK_2rVhaztD8BxsbJTWZEDgKR3h6PSH3JBpI_valRNtAfY8FEgd_w8y3cVizgLdjUyp1g-GrPMpsDb7URN2J6AQHZj8JjwibeCrZvS0e9VEnJllEC2kCYRQJMyDd-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/cg74HnwWCdgQ4FUrJsbKr9ovBsBJB6MTFMcQAheR4gl4rEuTcwiDbFLERECdJveIyA_dpFP7Oz0gw2jZg1Vc36RCjDTW2Bb5WY5mxxo2Gl3CntFBvliNSXwtU4TwxtqAphuBvTHvtI_QdGU15_NohGk-0rvawTGIbC9fmfi49vZE4qtaVeqMp3a9sL6l5fLq?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/uXliehbi-vTr-H8xYrnREkLUDzpCaY9dmorOC_JGEReqZ7juUqdpRvz5CNQWbzxo70Buq_fYENvMDu2Z6Y8VYVwA-W_TCl1nq_9OrYLDUOcFCndR4VK5JeuqFfn5V-ae4egcGFhIFpFFEkO7YHA9y7UGq-o1ups0wapwebDT-Y8zCF3vGWmpBexUZXFKx5h-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/0EEqGw6NmdMQY4WlAtCNFxt3k0tNgFLr8gTh5UHBYrKcgAVpjPRm_wmueSJwGqfhB1S42RW3RKqhUMz8UNNWD_4aIGrBxXodOtOtJ-CbGNpxe8LMPi9DXlUVgtmkig9XKl_tOwkromLijKiKnTcKixErBLG-Y9UzeX8lzMRxJOzyISk3_oprJYs6lXdwtrbD?purpose=fullsize)

- Fetches **stock prices**
- Provides **analyst recommendations**
- Uses **tabular markdown outputs**

```python
tools=[YFinanceTools(), DuckDuckGoTools()]
```

📄 Source:

---

### 🧠 3. Memory-Enabled Agent (Persistent Intelligence)

![Image](https://images.openai.com/static-rsc-4/ag_c-yiJw-o3yhRtPTAYG19OM77BIqJEthq-auV6RkurPfcsO_Rz9499ya8cINIY808D6uCo6EjNPgTYK8rm8dCPOy1rkE1ho-wrvb1EOGzPXwtj9zPwZCw5c6zEN6D94d5hoeGcXtJovHy98Mpyyx6HN_pkXRhfoyXX_CupwH6HSv_AVA8rmKWmCeCd1Tpb?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/QnIEHWw-Jz_11lGzVCJ3tmFkxgZqdC-tj_y4ZH6iOxj2_JvwFx_SYN4Tk8__tbSl0Aglmq44nhWjmMJVW9wpDYQzbTFgDgkEfkgelQFhyfe2kef8hmhyjkyXb7FRTh7Eaipe1wpLsVvnNUQSTbF7dzKoTFGAjWJa4qghU9DVTSjP4Hmj5Rf4XBLGEq8phDa-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/IeueejlMAikyb3rmoLg4aiAWseSnoyB-HbtXbBd2qH87bERspzZiQex0XqP8Ue4MKjFL_60MlYEtAKaMjuHQB2fC-GCFgowVCwYioVpZ6v0pKn_vBVut2a_ZHv39I2gA8PD1yUFYmVqiQPBsUDjiPO52jSlhX9ejX2R6w9CDbws_mWlv_oDkiEmn9_FPrGMt?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/TjKuWJOaQ59RXDeK1lD6IGn_jcFRwouL9BpVlByNWkYOlPJ6bjomtN5JxqDnpjx17YTHwNoweEmMGzeQ0r8IgiTwsH2AX20zL5ACdygfuHtQzXjka2reaDu-1wZw4wvCetrc4c81rvyNnFVY3m5DcsbBUWsP3YH0W1NsUsxek4jT6EzFU6cZY71M-0Cw17XY?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/B3Ksec1m5hLKQNM8gjcf76Koi3t9eco8TWTv6Sq9ZrCluQ4QXz9X0uQ2YIbL0OFS67bAOA_pBQNcM35ldkRxtR8TntDsaqkuN8p9zs8l8P1EIGtPqJJDxktCBtoeRTOTNNzVM0c8JeTa3l-ocoew-kOKqFj9tDHRkmsylUZdtQN_tIpa5YShl-wC31vXuPSc?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/B0dncVDZcRSY7QcDojSJgfAj6ymVV9A0nb5Ta-MBzXSQ_KxkPIpRazRj5iPfyOsjunBzFpZmF85VQ_fkMCyX4c9-gTFbBL3lmF1K3BPHlZMBXyEJW73I9EubIVrGEgp77bHDtn85FrjMBhShskjM2AKoMFezg2stMXaiJ9G0Xumb5HnBLw94TsYIZuvtcDzn?purpose=fullsize)

- Stores user data in **SQLite**
- Retrieves past interactions
- Enables **personalized AI**

```python
enable_user_memories=True
add_history_to_context=True
```

📄 Source:

---

### 👥 4. Multi-Agent System (Team Collaboration)

![Image](https://images.openai.com/static-rsc-4/vWvj1NQl_4nOwvYYh2EZcxro0fnvgVlU7E4fvhsBKeT3dlFAG4fBNJgtNpJhKZHsJ6AOF81QwSBKznIdJW6lbGhGjVujYOMW9Wiy5aahSbZWMbV2-jbSKQgp2AvuGSTGMGb7l6uwS-uE149QxFAPoQyy7vKu-YBwcWOpbmOYs-Q8POq6lt6SxwV0J6W32CVG?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/MHP4yeRYpVhm2mzkmmaChkhtuU7wFQ-QlhHlO41LD3HPRy4yyROHUrR9HOvQI1hIpFhDFCqWV7RMiGpcfq1JkoXq8AsRKxWfiAcww8AhpB2gLJEDQEUn4pJsYbA0YNXURM7GxTtm-mUfMwVhZEqwe2QOPyBFk7FD5mS-voSUQUUlbHfda1o8-Q-lPvpORjtj?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/WmgaMqBEcUDW-Wuubl1pDl4yTZXvOf2vAoylQy4SOPzu2wz3HxmY9hrAE8PXakZ8TjiYHw1Pf4Z9dNFLenUgCR7K2xjqZ8tDYgNG0Lfa3ITzx8cnY4D0_Rbs3NWjxfD6rMiUrk1AtAyM3vF8btKUoUmPBJnh5-ZHFbMoK5cm7eEWR9INjDDBVELWu6plTwkJ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/EmmrHEB_4l8EjvfQ5EpTnVNxAcKelrBT34ijkbXRsVV-IpzKQykRrvDQAulodR9M5hhpe5wQU8cU_xFi_nYEUwDBLqmJ7R_3pjdnNl9VPLoinDXobaP8p-qZHKYXewKGAcq4jGkjrqghNWaHiL5zreRpnFk0vY-M1bmZkL3FJGkJaMawyarqhLD25U3wvmx-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UL7w0V1pRh7hGj_Ac13xDKiOKlItDWOqQeNHobwpOMneAD2XbVuW4eolbhkfvV0iSQPnmZS3hi8gMEztDMuni-9T8OdFQJr9L9Wem1QA3KyinF4Tr1X4Akm3VCga6Dz0y7TKVCzOXccGF6zgqacrgeMyQPtlqqLE_upvIDHcNGsyHThGWq-j4Re-AUCatsEy?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/fGKrgTLQFVGWOnlkLGR5zK55xZtu4-ZZswhyHTWy-n9ATniFDV2QsN9IQ_mzKZno0oN-LSCmxLnkrm58Ek5eKdA6vzbEdfCYNQ2yHIMS7hMdSDBfUq21ULiEHoilzegNAaIPtVKMDCnoxOkt9d_weoyENYd4WXfWreNdpgz953xK91FSY9HHPAZDmLQ9FsfE?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ErH0vD7bmF1OdtoxIcKhYKNJWjlrZ5e9d6dHX8TvisWlzWrETEmg0ocLycWOG1KxwDYZs-jLIxdaTuEbglRJtJ4-8t7t-R5FabsgZyr_2rfhIS5IXEMMLsz2dUiMQMUYVUXy_YfyqS5oe6ZTFET5ouYYn2fb3YaG_MPETjuS9VlO6tzt0fCUlJFH6i2tYTng?purpose=fullsize)

- Multiple agents:
  - English 🇬🇧
  - Chinese 🇨🇳
  - Hindi 🇮🇳

- Coordinated via **Team Leader**
- Parallel responses

```python
Team(
    members=[eng_agent, chi_agent, hindi_agent],
    instructions="All agents must respond"
)
```

📄 Source:

---

### 🎥 5. YouTube Video Analyzer Agent

![Image](https://images.openai.com/static-rsc-4/KQ5VG86UsQE9UisNxXS9geJ_zYsMgb9nxSdgv3AcJxagiT7lzySjou3H16zcBKDeEc2At-NCUUQQKzgAlSz_DQupxsA3CloNOJlUVwmE05lbyGY_s_4Vuf9dZlYN7dbGN-sgveTVAiL8HlDnni5FRKCK-8MPdnHjD12IUICWfFB76ZmmNp1_laF9jTjjG-gF?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Le0Al9WFGQnFNRlmRQrvFhhpYqhRc7kHi4_iC2jOJCS31IkgN3aBNkPjvVPrcKa28XWtTZ7OaisC3ldFhFoS8Ri9OYB-UPwxidk-rn6eDxxCcWqaCKom9Nm-W3JzYb4TmfdlFJkUClSdEVbazo3wHeT7Qe87bzi3TKd0CTa1kF2fD4qNI2a3QYhvY6wCAfo2?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/fyAtyIaYzpxcjtn-4JxdaURkfoERrl2auizRsz2UyhRnPDLT9vpjf2M96lzEj1NIyUaChHnWKl0YEDF3ZZVUIaYPwhm_8eL1vljNOl_CBMPuHSfnvUFNuVBsyzGICLXsZolfjJNnMJ0JIoOD0wVlMmeHRZTuEVfdRqWWw4veHXAgEOgjh7C7z1d6pu6WGUxt?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ZUSV0tDz3L4HWv0532pbSw9snOgaLzhrK1I2Z793Pj4gl4eE56_jBTKEqYZGo4CKElgLNHeWOgoBWZ4uzd_Xa0ab487hqvOrpn5waQ07l8LM27t4CqvUwpi6gIEjp-7-hSzYgYnxZ_a_G_U7ZCDtnGnTqxDy4nnYecq3o1GnZDFPw8VReLX_6CBn1mYK_nYP?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/P3CBaOBVBg3tFKB3Aw58QiX95nbyNa5bfYIHYDWJYk8XkU-15-fN6jgiJKhmGA8pH6Reg3XQ6mcWu-O6fPVhzbvy_Bp55L5so3CF9IStEnb0N9I9-P8QnwKllc7mNEYMkVom5SwuOBvyAU-KFOVzxmkd1KqGBEeWRA9NWvtyqTifGic2-cM9HU-2py5jbpeA?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ePcXumbRoDFbo8jinftifkCF4Cw5DRXcKRMfO_VIoHzoqerj9_1vNRxl6aVlnMKbiO9TAF9QFSs1l9__ED3F61cZEkGTjCTkK6v8kosfcCsfrf3UjHQ5Uj8-IU6zPC0IaBCXA6PY-6LboNy12Kf_xIiJVh8NphnKSShNKFueaddg52yN9DfipJXXbfZ9HSQY?purpose=fullsize)

- Extracts:
  - Metadata
  - Timestamps
  - Topic segmentation

- Uses **OpenAI + YouTube tools**

📄 Source:

---

### 🌐 6. Streamlit Deployment (Real App)

![Image](https://images.openai.com/static-rsc-4/B9vKkgGEbrOUsRbi7cqQjYzcEGY1E1a5eFtw6IvcmrybRD4J-Vag9tu-xouRXtTrByE3QXilk5t5KUZKyZubxSNx-Vh_H1vedG7thjQ40rlzd65YQ3kI36IyOZqKAypeg0XjURPk27wU6ICzvFWAkwOq3r1HW22dw7ib77Sp9J1Ft7uz38hLvvfZmVAB5v3j?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/i4P4btSfkqtoGu21z8mcSuALDEXtVkFaE8CGCuCaFysARZMtrZyG3YAca3kaxlqYRJuddwPLHwb65Seg9_UyWFAhyq0RTLxzdQatbQ6YmjIEVxnYa10xzoo2DOU55bcyIZVYbBKK2QHfd8KSSulplam-lv_biWtBBBE_pe3x38QGcFRSMR0KYmrpc2yAyNNF?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/udzNnQeX7BUZowzJKXLxasLgWk8AHYHYDbqfm6--Cx8wl2e0AIuiqnj15XdHlv1TZexlw9Jwx-JEzfqYJNDwHYKc7rPJfcjgQ4OSQRSv9Z3vIefonzqWqb36f1Gmyqyu4Rz2CMtW1XqYZLiG_sxNm0SwYC3u3g-lmsZeN9ejHgzVpi7qjJOLzzH1UGjJY4-a?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/7dI9hkYolxtmU_0qMv_kKUPvQG8LX3QwMQu2Cfr3L53ecjtbZm0mliCoRSIqTFjn3P98qOR0NjdQuShzaszq4Dx0qE88Gxq2qivOwsjB3qWSY9QR9xgoFl90MM1Sbc4_fl2jQiPLitEpgTaBOE0Ip2Igpa8Zozb5c7e-c3Nd3naxCSu_KjtyKrjvdnPH2zd-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Et1wspfW6qUjJJEs6Bko8TI9q5zsRTv0cPmUhws-mGhpzb_eOqvdTPy0wRND2UI4OtnKcSbVbIDUbUmaL-p9tR7X0Cre7P5fWi2bHIBWUBXg4NNRxG2atYtz8raRivYZmHhzRe2eEe3_OIo9jMCbHohK-zELxSTp4ybOE15BHTElXT6CL2Mz5b9dhIbuIas7?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/x5sBtejGJJjxainpSBN9tCIZhAYc5oHmwmBHLtwF8up2D_X6Ts2ttkFedSU38zlsHfD5EtsuggZE-4icj6gtPfet4MmmQjNj0BOj3wKufeabMywjgTzG4bQKb3fzGpWF38uemsAwM8qxUU0Z_ZcPtSfTqs13IQfFpwsRdqsNIWHtinsPDERTy1uZKfyeDw0j?purpose=fullsize)

- Interactive UI
- Real-time agent execution
- Cached agent loading

```python
video_url = st.text_input("Enter Youtube Video Link")
```

📄 Source:

---

## 🔄 End-to-End Workflow

```text
User Query
   ↓
Agent (LLM + Instructions)
   ↓
Decision Making
   ├── Tool Use
   ├── Memory Retrieval
   └── Multi-Agent Routing
   ↓
Execution
   ↓
Structured Response (Markdown/UI)
```

---

## 🧪 Real Use Cases

- 🌍 Travel safety recommendations
- 📈 Stock analysis & investment insights
- 🧠 Personalized assistants with memory
- 🌐 Multilingual AI systems
- 🎥 Automated YouTube content analysis

---

## ⚠️ Challenges Faced

- Tool selection reliability
- Prompt engineering complexity
- Memory consistency handling
- Multi-agent coordination
- Debugging agent workflows

---

## 📈 Key Learnings

- **Agent = LLM + Tools + Reasoning + Memory**
- Memory transforms stateless LLMs into **stateful systems**
- Multi-agent systems enable **parallel intelligence**
- UI deployment is essential for **real-world usability**
- Prompt design directly impacts **agent behavior**

---

## 🔮 Future Enhancements

- 🔹 Retrieval-Augmented Generation (RAG)
- 🔹 Vector DB (FAISS / Pinecone)
- 🔹 Autonomous planning agents (AutoGPT-style)
- 🔹 Voice-based agents
- 🔹 FastAPI + Docker deployment

---

## 👨‍💻 Author

**Satinder Singh Sall**
_AI/ML Engineer | Agentic AI Specialist_

📍 Prime AI/ML Batch
📅 April 2026

---

## 🏁 Conclusion

This project demonstrates a **complete transition from LLM usage → Agentic AI systems**, covering:

- Tool usage
- Memory
- Multi-agent collaboration
- Deployment

> 🚀 _Agentic AI is the foundation of next-generation intelligent systems._

---

## ⭐ Portfolio Impact

This project showcases:

- ✅ Real-world AI system design
- ✅ Multi-agent orchestration
- ✅ Production-ready deployment
- ✅ Strong understanding of modern AI paradigms

---

# 🤖 Agentic AI Systems with Agno Framework

> **Academic + Portfolio Project | Prime AI/ML Batch**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LLM](https://img.shields.io/badge/LLM-Groq%20%7C%20OpenAI-green)
![Framework](https://img.shields.io/badge/Framework-Agno-orange)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

## 📌 Overview

This project demonstrates the design and implementation of **Agentic AI systems** using the **Agno framework**, focusing on building intelligent, tool-using, and collaborative AI agents.

The work spans from **basic agents** to **multi-agent systems**, including:

- Tool-integrated AI agents
- Financial analysis agents
- Memory-enabled agents
- Multi-agent collaboration (Teams)
- YouTube video analysis agent
- Streamlit-based deployment

---

## 🎯 Objectives

- Understand the concept of **Agentic AI**
- Build **autonomous AI agents with tools**
- Implement **multi-agent collaboration systems**
- Enable **memory and context awareness**
- Deploy AI agents using **Streamlit UI**

---

## 🧠 Key Concepts Covered

### 🔹 1. Agentic AI Fundamentals

- Difference between traditional LLMs vs agents
- Tool usage and decision-making
- Context-aware reasoning

### 🔹 2. Tool-Integrated Agents

- Search tools (DuckDuckGo)
- Financial data tools (Yahoo Finance)
- YouTube data extraction

### 🔹 3. Multi-Agent Systems

- Agent collaboration
- Task distribution
- Role-based responses

### 🔹 4. Memory in Agents

- Persistent memory using SQLite
- User-specific context retention
- Conversational continuity

### 🔹 5. AI Deployment

- Streamlit-based UI
- Interactive applications
- Real-time inference

---

## 📂 Project Structure

```bash
.
├── agent.py                 # Basic tool-enabled agent (travel assistant)
├── finance.py               # Financial analysis agent
├── memory.py                # Agent with persistent memory
├── team.py                  # Multi-agent collaboration system
├── youtube_analyzer.py      # YouTube analysis agent
├── ui.py                    # Streamlit frontend
├── README.md                # Project documentation
```

---

## ⚙️ Tech Stack

| Category    | Tools / Libraries             |
| ----------- | ----------------------------- |
| Language    | Python                        |
| Framework   | Agno                          |
| Models      | Groq (Qwen), OpenAI           |
| Tools       | DuckDuckGo, YFinance, YouTube |
| Database    | SQLite                        |
| UI          | Streamlit                     |
| Environment | dotenv                        |

---

## 🚀 Core Implementations

### 🔹 1. Basic Agent (Tool-Enabled)

A travel assistant agent that uses search tools for real-time information.

- Uses **DuckDuckGo tools**
- Adds **date-time context**
- Responds in **Markdown format**

📄 Reference:

---

### 🔹 2. Finance Agent 📈

An intelligent financial analyst agent that:

- Fetches stock data
- Provides analyst recommendations
- Uses structured markdown output

📄 Reference:

---

### 🔹 3. Memory-Enabled Agent 🧠

Implements **persistent memory** using SQLite:

- Stores user identity
- Retrieves past interactions
- Enables personalized responses

📄 Reference:

---

### 🔹 4. Multi-Agent System (Team) 👥

A collaborative system with multiple agents:

- English Agent
- Chinese Agent
- Hindi Agent

All agents respond simultaneously under a **team leader**.

📄 Reference:

---

### 🔹 5. YouTube Video Analyzer 🎥

An advanced agent that:

- Extracts video metadata
- Generates timestamps
- Provides structured content analysis

📄 Reference:

---

### 🔹 6. Streamlit Deployment 🌐

Interactive UI for real-world usage:

- Accepts YouTube links
- Displays AI-generated analysis
- Uses caching for performance

📄 Reference:

---

## 🔄 System Architecture

```
User Input
   ↓
Agent (LLM + Instructions)
   ↓
Tool Selection (Search / Finance / YouTube)
   ↓
Execution
   ↓
Response (Markdown / Structured Output)
```

---

## 🧪 Example Use Cases

- 🌍 Travel safety recommendations
- 📊 Stock market insights
- 🧠 Personalized assistants with memory
- 🌐 Multilingual responses
- 🎥 Automated video analysis

---

## ⚠️ Challenges Faced

- Tool selection accuracy
- Managing multi-agent coordination
- Memory consistency
- Prompt engineering for reliability
- Debugging agent workflows

---

## 📈 Key Learnings

- Agents are **LLMs + tools + reasoning**
- Memory significantly improves user experience
- Multi-agent systems enable **parallel intelligence**
- Prompt design directly impacts performance
- Real-world deployment requires **UI + backend integration**

---

## 🔮 Future Enhancements

- 🔹 Add RAG (Retrieval-Augmented Generation)
- 🔹 Integrate vector databases (FAISS / Pinecone)
- 🔹 Add voice-based interaction
- 🔹 Improve agent planning (AutoGPT-style)
- 🔹 Deploy using FastAPI + Docker

---

## 👨‍💻 Author

**Satinder Singh Sall**
_AI/ML Engineer | Agentic AI Enthusiast_

**Course:** Prime AI/ML Batch
**Module:** Agentic AI
**Date:** April 2026

---

## 📄 License

This project is intended for **academic and educational purposes only**.

---

## ⭐ Portfolio Note

This project demonstrates:

- ✅ Practical implementation of **Agentic AI systems**
- ✅ Experience with **LLM orchestration frameworks**
- ✅ Ability to build **production-ready AI applications**
- ✅ Understanding of **multi-agent collaboration & memory systems**

---
