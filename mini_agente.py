import os
import sys
from groq import Groq
from dotenv import load_dotenv


def inicializar_cliente():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        print("❌ ERRO: Chave GROQ_API_KEY não encontrada!")
        print("📝 Crie um arquivo .env com: GROQ_API_KEY=sua_chave_aqui")
        sys.exit(1)

    return Groq(api_key=api_key)


def gerar_plano(cliente, tarefa):
    prompt = f"""
    Você é um agente planejador especializado.
    Gere um plano simples, direto e passo a passo para a seguinte tarefa:
    "{tarefa}"

    Use etapas curtas, práticas e numeradas.
    """

    try:
        resposta = cliente.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return resposta.choices[0].message.content

    except Exception as e:
        return f"❌ Erro ao gerar plano: {str(e)}"


def exibir_banner():
    print("\n" + "=" * 60)
    print("🤖  MINI AGENTE DE PLANEJAMENTO COM IA")
    print("=" * 60)
    print("Descreva sua tarefa e receba um plano de ação detalhado!\n")


def main():
    exibir_banner()

    cliente = inicializar_cliente()

    print("💡 Exemplo: 'criar um aplicativo web de tarefas'")
    tarefa = input("📋 Digite o que você quer fazer: ").strip()

    if not tarefa:
        print("⚠️  Nenhuma tarefa fornecida. Encerrando...")
        return

    print("\n⏳ Gerando plano...\n")
    print("-" * 60)
    plano = gerar_plano(cliente, tarefa)
    print(plano)
    print("-" * 60)
    print("\n✅ Plano gerado com sucesso!\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {str(e)}")
        sys.exit(1)