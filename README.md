# dog-finder
Finding your puppy with image search

## Details

List of dogs in our dataset
<img width="1322" height="865" alt="image" src="https://github.com/user-attachments/assets/432c5f86-c515-4593-b104-fb1dd2435916" />

Lost Dog image:
<img width="623" height="662" alt="image" src="https://github.com/user-attachments/assets/03de6fff-9d15-4d1c-9e85-e89518c44bfc" />

After Running the main with `python src/main.py` it found the right puppy named Luigi:
<img width="526" height="513" alt="image" src="https://github.com/user-attachments/assets/e9dd0fdf-5a4b-445f-abb0-d3af231006e9" />


## How to run
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/dog-finder.git
   ```
2. Navigate to the project directory:
   ```
    cd dog-finder
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Set up elasticsearch (optional if you want a local elasticsearch instance):
    ```
    sh elastic-launcher.sh
    ```
5. Configure the application:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file to set your configuration variables.
   (Optional) Head over to the last step to get the necessary credentials.

6. Run the application:
    ```
    python src/main.py
    ```
