from fastapi import FastAPI, HTTPException
from data.load_csv import LoadCsv



app = FastAPI()



@app.get("/csv/preview")
def return_data_frame():
    """
    Return the current dataset for preview.

    Returns:
        dict: Dataset as list of dicts and index column name.

    Raises:
        HTTPException: If reading data fails.
    """
    try:
        csv = LoadCsv()
        data = csv.read_data_csv()
        name_index = data.index.name or "index"
        main_server_logger.info("Returning dataset preview.")
        return {"result": data.reset_index().to_dict("records"), "name_index": name_index}
    except Exception as e:
        main_server_logger.error(f"Failed to return dataset preview: {e}")
        raise HTTPException(status_code=500, detail="Failed to return dataset preview.")

