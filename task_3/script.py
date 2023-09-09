import os
import tarfile

# Путь к каталогу /etc
source_directory = "/etc"

# Папка назначения для архивов
backup_directory = "/etc/bkp"

# Получение списка подкаталогов, начинающихся с "cron"
cron_directories = [entry for entry in os.listdir(source_directory) if entry.startswith("cron")]

# Создание каталога назначения, если он не существует
os.makedirs(backup_directory, exist_ok=True)

# Создание архивов для каждого каталога и сохранение их в /etc/bkp/
for directory in cron_directories:
    source_path = os.path.join(source_directory, directory)
    backup_filename = os.path.join(backup_directory, f"{directory}.tar.gz")

    # Создание архива tar.gz
    with tarfile.open(backup_filename, "w:gz") as archive:
        archive.add(source_path, arcname=os.path.basename(directory))
