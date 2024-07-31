# Google-Dorking
![Screenshot](https://github.com/Thisishivam/google-dorking/blob/main/dork-help.png)


# Dork Tool

Dork Tool is a Python script that allows you to perform Google dorking, which is a method of using advanced search operators to find specific information on the web using the Google search engine.

## Prerequisites

- Python 3.x
- `pip` package manager

1. Clone the repository:

   ```shell
   git clone https://github.com/Thisishivam/google-dorking
   ```
2. Navigate to the cloned directory:

   ```shell
   cd google-dorking
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

   
## Usage

1. Run the script using the following command:

   ```shell
   python dork.py <search_query> --num_results <number_of_results> --delay <number_of_delay>
   ```

   Replace `<search_query>` with your desired search query. Enclose the query in quotes if it contains spaces or special characters.

2. The script will retrieve the search results from Google and extract the URLs matching the search query.

3. The extracted URLs will be printed to the console as well as it will be stored in a file.
   
![Screenshot](https://github.com/Thisishivam/google-dorking/blob/main/dork-result.png)

## Disclaimer

Please use this tool responsibly and adhere to the terms of service of the search engine you are using. The Dork Tool is intended for educational and informational purposes only. The authors are not responsible for any misuse or illegal activities performed using this tool.
