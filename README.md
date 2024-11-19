# LegalLLM: A Multi-Task Large Language Model for US Legal Analytics

## Current Status
LegalLLM has successfully implemented its core functionalities:  

1. **Similar Case Retrieval (SCR):** Users can retrieve relevant cases based on input queries or details.  
2. **Precedent Case Recommendation (PCR):** Identifies and explains the most applicable precedent cases.  
3. **Legal Judgment Prediction (LJP):** Predicts judicial outcomes with high accuracy based on historical data.  

### Pending Feature
The ability for users to upload PDFs or images of case documents for analysis is under development.  

---

## Baseline Modules Description

### 1. Similar Case Retrieval (SCR)
- **Purpose:** Identifies cases similar to the user-provided input.  
- **Implementation:** Uses semantic similarity algorithms on the CaseLaw dataset.  
- **Output:** Retrieves a ranked list of similar cases along with summaries and metadata.

### 2. Precedent Case Recommendation (PCR)
- **Purpose:** Recommends relevant precedent cases for the input context.  
- **Implementation:** Fine-tuned Llama 2.0 on legal texts identifies critical precedents.  
- **Output:** Presents the top precedents with detailed relevance explanations.

### 3. Legal Judgment Prediction (LJP)
- **Purpose:** Predicts potential outcomes of cases based on the input.  
- **Implementation:** Utilizes transformer models from the Hugging Face library to make predictions.  
- **Output:** Provides predicted verdicts with associated confidence scores.

---

## Screenshots

1. **Similar Case Retrieval (SCR)**  
   ![SCR Screenshot](path/to/screenshot1.png)  

2. **Precedent Case Recommendation (PCR)**  
   ![PCR Screenshot](path/to/screenshot2.png)  

3. **Legal Judgment Prediction (LJP)**  
   ![LJP Screenshot](path/to/screenshot3.png)  

4. **Web Application Dashboard**  
   ![Dashboard Screenshot](path/to/screenshot4.png)  

*(Replace the `path/to/screenshotX.png` with the actual file paths of your screenshots.)*

---

## References

1. [CaseLaw Dataset](https://case.law/)  
2. [Hugging Face Transformers Library](https://github.com/huggingface/transformers)  
3. [Llama 2.0](https://www.llama.com/llama2)  
4. [Revolutionizing Legal Research Paper](https://www.purplescape.com/revolutionizing-legal-research)  
5. [Legal NLP Research Paper](https://ieeexplore.ieee.org/document/10386911)  

---

## Challenges Encountered

### 1. **PDF/Image Upload and Processing**
- **Problem:** Implementing OCR to handle diverse legal document formats and quality.  
- **Reason:** Complex layouts and poor quality in scanned documents.  

### 2. **Dataset Size and Preprocessing**
- **Problem:** Managing and preprocessing large volumes of unstructured data.  
- **Reason:** Diverse formats and complex legal language in case records.  

### 3. **Model Performance**
- **Problem:** Optimizing inference speed and accuracy for real-time applications.  
- **Reason:** Balancing fine-tuning and latency on large models.  

---

## Plans to Overcome Challenges and Move Forward

### 1. **PDF/Image Upload Feature**
- **Plan:** Leverage OCR tools (e.g., Tesseract, Google Cloud Vision) to extract and process text.  
- **Next Steps:** Develop pre-processing pipelines to clean and format the extracted data.

### 2. **Dataset Optimization**
- **Plan:** Use distributed frameworks like Apache Spark for data processing.  
- **Next Steps:** Implement custom parsing scripts to standardize data structures.

### 3. **Model Performance Enhancement**
- **Plan:** Use model quantization techniques to reduce latency.  
- **Next Steps:** Optimize real-time inference with hardware accelerators like GPUs/TPUs.  

---

## How to Contribute
Contributions are welcome!  
- Submit issues or feature requests via the [GitHub Issues](https://github.com/LegalLLM/issues) page.  

---

> **Contact Information:**  
> For queries, reach out to the team:  
> - Danishbir Singh Bhatti: [danishbirsingh.bhatti@sjsu.edu](mailto:danishbirsingh.bhatti@sjsu.edu)  
> - Jay Shon: [seojun.shon@sjsu.edu](mailto:seojun.shon@sjsu.edu)  
> - Anthony Kommareddy: [anthonysandeshreddy.kommareddy@sjsu.edu](mailto:anthonysandeshreddy.kommareddy@sjsu.edu)  
