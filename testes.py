database_name = "your_database_name"  # Substitua pelo nome do seu banco de dados
    table_name = "your_table_name"  # Substitua pelo nome da sua tabela

    client = boto3.client('glue')

    response = client.get_table(
        DatabaseName=database_name,
        Name=table_name
    )

    table_properties = response['Table']
    s3_location = table_properties['StorageDescriptor']['Location']

    print("A localização da tabela no S3 é: ", s3_location)
