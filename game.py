print("🔥 GAME INICIOU") 
   class Game:
    def __init__(self):
        self.position = "entrada"
        self.running = True

    def show_status(self):
        print("\n🧊 Você está no frigorífico abandonado")
        print(f"📍 Local atual: {self.position}")

    def move(self):
        print("\nPara onde você quer ir?")
        print("1 - Câmara fria")
        print("2 - Corredor")
        print("3 - Sala de máquinas")

        choice = input("> ")

        if choice == "1":
            self.position = "câmara fria"
        elif choice == "2":
            self.position = "corredor"
        elif choice == "3":
            self.position = "sala de máquinas"
        else:
            print("❌ Movimento inválido")

    def play(self):
        while self.running:
            self.show_status()

            print("\nAções:")
            print("1 - Andar")
            print("2 - Sair")

            action = input("> ")

            if action == "1":
                self.move()
            elif action == "2":
                print("👋 Saindo do jogo...")
                self.running = False
            else:
                print("❌ Opção inválida")


game = Game()
game.play()
