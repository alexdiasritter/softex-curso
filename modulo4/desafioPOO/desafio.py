# SIMULADOR DE REDE SOCIAL (Versão Texto)
class Usuario:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido

class Post:
    def __init__(self, texto, dono):
        self.texto = texto
        self.dono = dono

class RedeSocial:
    def __init__(self):
        self.banco_de_posts = []

    def criar_post(self, texto, usuario_logado):
        novo_post = Post(texto, usuario_logado)
        self.banco_de_posts.append(novo_post)
        print(f" Post criado por {usuario_logado.apelido}!")

    def ver_meu_perfil(self, usuario_logado):
        print(f"\n --- PERFIL DE {usuario_logado.nome.upper()} ---")
        print(f" Usuário: {usuario_logado.apelido}")
        print("-" * 30)
        
        encontrou_algo = False
        for post in self.banco_de_posts:
            # CORREÇÃO: Só mostra posts do usuário logado
            if post.dono == usuario_logado:
                print(f" {post.texto} (Postado por: {post.dono.apelido})")
                encontrou_algo = True

        if not encontrou_algo:
            print(" (Nenhum post encontrado )")
        print("-" * 30 + "\n")

# --- ÁREA PERSONALIZADA ---
usuario_principal = Usuario("Carlos Silva", "@carlinhos_tech")
usuario_secundario = Usuario("Ana Souza", "@ana_gameplays")

minha_rede_social = RedeSocial()

minha_rede_social.criar_post("Hoje aprendi Python e consertei um bug social! 🐍", usuario_principal)
minha_rede_social.criar_post("Novo recorde no jogo: 999 pontos! 🎮", usuario_secundario)
minha_rede_social.criar_post("Alguém mais viu a nova série da Netflix?", usuario_principal)

print("\n--- TESTANDO SEU CÓDIGO ---")
minha_rede_social.ver_meu_perfil(usuario_principal)