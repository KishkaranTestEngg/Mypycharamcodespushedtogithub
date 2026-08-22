from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------------------------------------------------
# TASK 12 - GUVI XPath
# Relative XPath + XPath Axes
# ---------------------------------------------------------

# Browser setup
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

# GUVI Home Page
driver.get("https://www.guvi.in/")

print("GUVI Page Title:", driver.title)
print("Current URL:", driver.current_url)


# ---------------------------------------------------------
# Helper method for single element operations
# ---------------------------------------------------------
def find_and_print(xpath, description):
    """
    Finds an element using XPath and prints its details.
    """
    try:
        element = wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        print("\n----------------------------------------")
        print(description)
        print("XPath:", xpath)
        print("Tag:", element.tag_name)
        print("Text:", element.text.strip().replace('\n', ' ')[:100])
        print("Displayed:", element.is_displayed())
        print("----------------------------------------")
        return element

    except Exception as e:
        print("\n----------------------------------------")
        print(description)
        print("XPath:", xpath)
        print("FAILED: Element not found or does not exist for this axis layout.")
        print("----------------------------------------")
        return None


# =========================================================
# PART 1 - BASIC RELATIVE XPATH
# =========================================================
print("\n\n========== RELATIVE XPATH ==========")

find_and_print("//p[normalize-space()='Courses']", "1. Courses - Relative XPath")
find_and_print("//p[normalize-space()='LIVE Classes']", "2. LIVE Classes - Relative XPath")
find_and_print("//p[normalize-space()='Practice']", "3. Practice - Relative XPath")
find_and_print("//p[normalize-space()='Resources']", "4. Resources - Relative XPath")
find_and_print("//p[normalize-space()='Our Products']", "5. Our Products - Relative XPath")
find_and_print("//button[normalize-space()='Login']", "6. Login - Relative XPath")
find_and_print("//button[normalize-space()='Sign up']", "7. Sign up - Relative XPath")

# =========================================================
# PART 2 - RELATIVE XPATH OPERATIONS
# =========================================================
print("\n\n========== RELATIVE XPATH OPERATIONS ==========")

# A. Parent
find_and_print("//p[normalize-space()='Courses']/parent::*", "A. Parent of Courses")

# B. First Child (Targeting the parent wrapper's child since plain text <p> holds no sub-tags)
find_and_print("//p[normalize-space()='Courses']/parent::*/*[1]", "B. First child of Courses wrapper")

# C. Second Sibling (Using following-sibling on the structural parent item)
find_and_print("//p[normalize-space()='Courses']/parent::*/following-sibling::*[2]",
               "C. Second sibling of Courses wrapper")

# D. Parent of an element having href (targeting anchor elements inside body layout instead of head tags)
find_and_print("//body//*[@href]/parent::*", "D. Parent of a visible body element having href")

# =========================================================
# PART 3 - XPATH AXES
# =========================================================
print("\n\n========== XPATH AXES ==========")

# 1. Parent Axis
find_and_print("//p[normalize-space()='Courses']/parent::*", "1. Parent Axis - Courses")

# 2. Child Axis (Targeting parent elements containing children nodes)
find_and_print("//p[normalize-space()='Courses']/parent::*/child::*", "2. Child Axis - Courses wrapper elements")

# 3. All Ancestors
find_and_print("//p[normalize-space()='Courses']/ancestor::html", "3. Ancestor HTML element of Courses")

# 4. All Following Siblings
find_and_print("//p[normalize-space()='Courses']/parent::*/following-sibling::*",
               "4. All Following Siblings of Courses wrapper")

# 5. All Preceding Elements
find_and_print("//p[normalize-space()='Courses']/preceding::div[1]", "5. First Preceding Div Element of Courses")

# 6. Following Axis
find_and_print("//p[normalize-space()='Courses']/following::div[1]", "6. First Following Div Element of Courses")

# 7. Preceding Sibling Axis
find_and_print("//p[normalize-space()='Courses']/parent::*/preceding-sibling::*",
               "7. Preceding Sibling Axis - Courses wrapper layout")

# 8. Descendant Axis
find_and_print("//p[normalize-space()='Courses']/parent::*/descendant::*",
               "8. Descendant Axis - Under Courses wrapper context")

# =========================================================
# PART 4 - PRINT ALL MATCHED ELEMENTS
# =========================================================
print("\n\n========== AXES MULTI-ELEMENT DETAILS ==========")


def print_all_elements(xpath, description):
    try:
        elements = driver.find_elements(By.XPATH, xpath)
        print(f"\n>>> {description} (Found: {len(elements)} elements)")

        # Display details for the first 5 elements to keep logs clean
        for index, element in enumerate(elements[:5]):
            tag = element.tag_name
            text = element.text.strip().replace('\n', ' ')[:50]
            print(f"  [{index + 1}] Tag: <{tag}> | Text snippet: '{text}'")

        if len(elements) > 5:
            print(f"  ... and {len(elements) - 5} more elements.")

    except Exception as e:
        print(f"\n>>> Error reading multi-elements for {description}: {e}")


# Example usages of multi-element evaluation
print_all_elements("//p[normalize-space()='Courses']/parent::*/following-sibling::*", "Following Siblings Checklist")
print_all_elements("//p[normalize-space()='Courses']/ancestor::*", "Full Ancestry Node Stack")

time.sleep(3)
driver.quit()
