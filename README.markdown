# Pomodoro Visual

A Python application implementing a Pomodoro timer with a graphical interface built using Tkinter. It offers two modes: a customizable conventional Pomodoro with focus and break intervals, and a continuous focus mode that tracks total focus time.

---

## 🇧🇷 Descrição (Português)

Este é um programa em Python que implementa um temporizador Pomodoro com uma interface gráfica visualmente atraente, construída com Tkinter. Ele suporta dois modos: o modo "Convencional", onde o usuário define os tempos de foco e descanso, e o modo "Foco", que conta o tempo total de concentração até ser parado manualmente.

### Funcionalidades
- Dois modos: Convencional (com ciclos de foco e descanso personalizáveis) e Foco (contínuo até parar).
- Interface gráfica com barra circular de progresso e exibição do tempo restante.
- Entradas para personalizar os tempos de foco e descanso no modo Convencional.
- Botões para iniciar, pausar e parar o temporizador.
- Efeitos visuais suaves, incluindo mudança de cores para foco e descanso.
- Notificações de fim de ciclo (foco ou descanso).
- Feedback de erros para entradas inválidas.

---

## 🇺🇸 Description (English)

This Python program implements a Pomodoro timer with an appealing graphical interface built using Tkinter. It supports two modes: a "Conventional" mode with customizable focus and break intervals, and a "Focus" mode that tracks total focus time until manually stopped.

### Features
- Two modes: Conventional (with customizable focus and break cycles) and Focus (continuous until stopped).
- Graphical interface with a circular progress bar and remaining time display.
- Input fields to customize focus and break times in Conventional mode.
- Buttons to start, pause, and stop the timer.
- Smooth visual effects, including color changes for focus and break periods.
- Notifications for the end of focus or break cycles.
- Error feedback for invalid inputs.

---

## Requisitos / Requirements

- Python 3.x
- Bibliotecas Python necessárias / Required Python libraries:
  - `tkinter` (usually included with Python)
- Sistema operacional / Operating system: Windows, macOS, or Linux

### Instalação / Installation
1. Certifique-se de ter o Python instalado / Ensure Python is installed.
2. Clone ou baixe este repositório / Clone or download this repository.
3. Execute o script `pomodoro_visual.py` / Run the `pomodoro_visual.py` script.

---

## Como Usar / How to Use

1. Execute o programa / Run the program:
   ```bash
   python pomodoro_visual.py
   ```
2. Na interface gráfica / In the graphical interface:
   - Escolha o modo: "Convencional" ou "Foco" / Select the mode: "Conventional" or "Focus".
   - No modo Convencional, insira os tempos de foco e descanso (em minutos) / In Conventional mode, enter focus and break times (in minutes).
   - Clique em "Start" para iniciar o temporizador / Click "Start" to begin the timer.
   - Use "Pause" para pausar/continuar ou "Stop" para encerrar / Use "Pause" to pause/resume or "Stop" to end.
3. No modo Convencional, o programa alterna automaticamente entre foco e descanso, com notificações / In Conventional mode, the program automatically switches between focus and break, with notifications.
4. No modo Foco, o tempo total é exibido ao parar / In Focus mode, total time is displayed upon stopping.

---

## Exemplo / Example

**Modo Convencional / Conventional Mode**:
- Configuração: 25 minutos de foco, 5 minutos de descanso / Setup: 25-minute focus, 5-minute break.
- Após 25 minutos, notificação: "Hora do descanso! 5 minutos." / After 25 minutes, notification: "Time for a break! 5 minutes."
- Após 5 minutos, notificação: "Volte ao trabalho!" / After 5 minutes, notification: "Back to work!"

**Modo Foco / Focus Mode**:
- Inicia e conta o tempo continuamente / Starts and tracks time continuously.
- Ao parar, exibe: "Tempo total focado: 01:30:00" (exemplo) / Upon stopping, displays: "Total focus time: 01:30:00" (example).

---

## Contribuições / Contributions

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias ou correções de bugs. / Contributions are welcome! Feel free to open issues or pull requests with improvements or bug fixes.

---

## Licença / License

Este projeto está licenciado sob a [MIT License](LICENSE). / This project is licensed under the [MIT License](LICENSE).

---

## Contato / Contact

Para dúvidas ou sugestões, abra uma issue no repositório. / For questions or suggestions, open an issue in the repository.