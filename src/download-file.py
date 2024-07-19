from ftplib import FTP


def download_file():
    # FTP server details
    ftp_server = "ftp.cdc.gov"
    remote_path = "/pub/publications/ART/"
    filename = "ART-2018-Clinic-Report-Full.pdf"
    local_filename = "ART-2018-Clinic-Report-Full.pdf"

    try:
        # Connect to the FTP server
        ftp = FTP(ftp_server)
        ftp.login()  # Anonymous login

        # Navigate to the specific directory
        ftp.cwd(remote_path)

        # Open the local file for writing in binary mode
        with open(local_filename, "wb") as local_file:
            # Define a callback to write the data to the local file
            def write_data(data):
                local_file.write(data)

            # Retrieve the file from the FTP server
            ftp.retrbinary(f"RETR {filename}", write_data)

        print(f"Successfully downloaded {filename} to {local_filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
    finally:
        # Close the FTP connection
        ftp.quit()


if __name__ == "__main__":
    download_file()
