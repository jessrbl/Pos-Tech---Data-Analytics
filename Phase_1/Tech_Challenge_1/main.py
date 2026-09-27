from src.data_loader import (
    locate_dataset,
    find_csv_files,
    load_datasets
)

#from src.exploratory_analysis import (
#    exploratory_analysis,
#    dataset_diagnosis,
#    analyze_keys,
#    validate_relationships
#)

def main():

    dataset_path = locate_dataset()

    csv_files = find_csv_files(dataset_path)

    datasets = load_datasets(*csv_files)

    #exploratory_analysis(datasets)
    #dataset_diagnosis(datasets)
    #analyze_keys(datasets)
    #validate_relationships(datasets)
    
    


if __name__ == "__main__":
    main()