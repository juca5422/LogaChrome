from seleniumbase import BaseCase

class MyTestClass(BaseCase):
    def test_open_youtube_with_profile(self):
        # Configuração do caminho para o perfil do Chrome
        user_data_dir = "C:/Users/SeuUsuario/AppData/Local/Google/Chrome/User Data"  # Substitua conforme necessário
        profile_dir = "Default"  # Ou o nome do perfil que você deseja usar
        
        # Adicionando argumentos de perfil ao Chrome
        chrome_options = [
            f"user-data-dir={user_data_dir}",
            f"profile-directory={profile_dir}"
        ]
        
        # Abrindo o navegador com as opções configuradas
        self.open("https://www.youtube.com", chrome_options=chrome_options)

    test_open_youtube_with_profile()