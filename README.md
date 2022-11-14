# Identifying the Purpose of the Tablet

## 🔁 Flow 
  Extract the text from user given tablet image using OCR( I use  <a href="https://github.com/PaddlePaddle/PaddleOCR" target="_blank">PaddleOCR</a> because of it's speed and accuracy) .Identify drug in OCR extracted text by using spatial information of the text . Finally scrap the **Drug Purpose** , **Drug Side Effects** and **Drug Price** from PharmEasy website.  
 
 
![image](https://user-images.githubusercontent.com/48553042/201034390-2a36fdf3-f949-4db2-8831-716cf8b442af.png)


## 	🖥️ Environmental setup

    git clone https://github.com/sukeshan/Identifying-the-purpose-of-the-tablet.git
    
    pip install -r Requirements.txt
  
 ## ⚡ Quick Inference
 
    from main import check
 
    check(file : image_path , drug_only : False) # If drug_only is True ,It will only return Drug name
  
  
