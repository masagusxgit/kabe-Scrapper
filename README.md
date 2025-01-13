This Python script scrapes categories and sub-categories from the website `https://www.kbcoco.com/` using Selenium WebDriver. The script performs the following tasks:

1. **Scrolls the page**: It ensures that all categories are loaded on the page.
2. **Clicks each main category**: For each main category on the page, it clicks to load sub-categories.
3. **Scrapes sub-category information**: For each sub-category, it captures the name and URL of the sub-category.
4. **Stores the data in a CSV file**: After collecting the sub-category data, it stores the information in a CSV file with columns for the main category, sub-category name, and URL.
5. **Allows the user to repeat the scraping process**: After the scraping is complete, the user can choose to repeat the process or stop.

---

### **Required Modules:**

To run the script, the following Python modules are required:

1. **Selenium**: For interacting with the webpage and automating the browser.
   - Install with: 
     ```
     pip install selenium
     ```

2. **Pandas**: For storing and saving data in CSV format.
   - Install with:
     ```
     pip install pandas
     ```

3. **ChromeDriver**: Selenium requires a browser driver (ChromeDriver in this case) to control Chrome. You need to download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure that it matches your version of Google Chrome. The script assumes that `chromedriver.exe` is located in the same directory as the script.

---

### **How to Use:**

#### **Step-by-Step Usage Instructions:**

1. **Download and Install Dependencies**:
   - Ensure you have Python installed.
   - Install the required modules using pip (see the "Required Modules" section above).
   - Download the correct version of ChromeDriver from the official website and place it in the same directory as the script.

2. **Set Up the Script**:
   - Make sure that the `chromedriver.exe` file is in the same directory as the script.
   - The script is set to use a headless Chrome browser (no browser UI). You can remove the headless option if you want to see the browser during execution.
   - Set the `url` variable to the webpage you want to scrape (in this case, `https://www.kbcoco.com/#/pages/goods/category/category?cateList=0`).

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script with the following command:
     ```
     python script_name.py
     ```

4. **Choose to Repeat or Stop**:
   - Once the script completes scraping the data, it will ask if you want to repeat the scraping process. Enter `y` to repeat the process or `n` to stop and save the data.
   - If you choose `n`, the data will be saved to a file named `kategori.csv` in the current directory.

---

### **Features:**

- **Scrolls to load content**: Ensures all categories are loaded before scraping.
- **Clicks each category**: Automatically clicks on each main category to load its sub-categories.
- **Stores data in CSV**: Saves scraped data (main category, sub-category name, and URL) to a CSV file.
- **Repeatable process**: Allows the user to repeat the scraping process for multiple runs before saving the data.

---

### **Script Flow:**

1. The script first navigates to the provided URL and performs a scroll to load all the main categories.
2. For each main category, the script clicks on it and collects all the sub-categories and their corresponding URLs.
3. After collecting the data for all sub-categories, the script asks if the user wants to repeat the process. If yes, the script restarts the scraping process. If no, the data is saved into a CSV file (`kategori.csv`).
4. The user can repeat the process multiple times before the final data is saved.

---

### **Example Output in CSV:**

After completing the scraping, the data will be saved in the following format:

```
kategori, sub_kategori, url
Main Category 1, Sub Category 1, https://www.kbcoco.com/...
Main Category 1, Sub Category 2, https://www.kbcoco.com/...
Main Category 2, Sub Category 1, https://www.kbcoco.com/...
...
```

---

### **Important Notes:**

- **Headless Mode**: By default, the script uses Chrome in headless mode, meaning the browser window will not be shown. If you want to see the browser during scraping, you can comment out the `options.add_argument("--headless")` line.
- **ChromeDriver**: Make sure to download the correct version of ChromeDriver that matches your installed version of Chrome.
- **Page Load Time**: The script assumes a small delay (`time.sleep(2)`) between actions to ensure the page content has loaded. You may need to adjust this depending on your network speed and the website's responsiveness.

---

With this script, you can efficiently scrape and store category and sub-category data from the `https://www.kbcoco.com/` website and easily repeat the process as needed.
