# Importando os módulos necessários do Kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Definindo a classe principal da aplicação
class MinhaApp(App):
    
    # Método para construir a interface do usuário
    def build(self):
        # Layout para organizar os widgets
        layout = BoxLayout(orientation='vertical')
        
        # Criando um botão
        botao = Button(text='Clique aqui!')
        
        # Ligando a função 'on_press' do botão a uma ação
        botao.bind(on_press=self.acao_botao)
        
        # Adicionando o botão ao layout
        layout.add_widget(botao)
        
        # Retornando o layout como a raiz da interface
        return layout
    
    # Função para a ação do botão
    def acao_botao(self, instance):
        print("O botão foi clicado!")

# Instanciando e executando a aplicação
if __name__ == '__main__':
    MinhaApp().run()
