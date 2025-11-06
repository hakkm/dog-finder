# dog-finder
Finding your puppy with image search

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
