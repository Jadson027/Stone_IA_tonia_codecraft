from datetime import datetime, timedelta

class CommemorativeTip:
    def __init__(self, date, occasion, tips):
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.occasion = occasion
        self.tips = tips

class CommemorativeDateChecker:
    @staticmethod
    def get_all_tips():
        tips_list = [
            CommemorativeTip("04/03/2024", "Carnaval", "Lanche Temático: Crie um hambúrguer ou combo especial inspirado nas cores e alegria do Carnaval, com ingredientes coloridos e sabores vibrantes.\n" +
                "Promoção para Blocos: Ofereça descontos para grupos de foliões que vierem ao fast food usando fantasias.\n" +
                "Combo de Carnaval: Monte um combo especial que inclua bebida refrescante, como suco ou refrigerante, perfeito para o calor do Carnaval.\n" +
                "Horário Estendido: Considere estender o horário de funcionamento para atrair foliões que estão saindo dos blocos.\n" +
                "Redes Sociais: Publique fotos dos combos e lanche temático de Carnaval, incentivando os clientes a compartilharem suas experiências na loja usando uma hashtag de Carnaval exclusiva."),
            CommemorativeTip("08/03/2024", "Dia da Mulher", "Desconto Especial: Ofereça um desconto exclusivo para todas as mulheres que visitarem o fast food neste dia.\n" +
                "Brinde para Elas: Inclua uma sobremesa grátis ou um item especial para todas as mulheres que fizerem um pedido.\n" +
                "Menu Saudável: Destaque opções de refeições mais leves e saudáveis no cardápio, voltadas ao público feminino.\n" +
                "Ambiente Acolhedor: Decore o espaço com flores e cores suaves para criar um ambiente agradável e especial para as mulheres.\n" +
                "Redes Sociais: Publique mensagens de homenagem ao Dia da Mulher, destacando as promoções e o ambiente especial do fast food, e incentive as clientes a compartilhar fotos com a hashtag do evento."),
            CommemorativeTip("15/03/2024", "Dia do Consumidor", "Combo com Desconto: Ofereça um combo especial com um preço promocional para atrair novos clientes.\n" +
                "Frete Grátis: Para pedidos online, ofereça frete grátis em todas as entregas do dia.\n" +
                "Bônus de Fidelidade: Dobre os pontos de fidelidade para os clientes que fizerem pedidos nesse dia.\n" +
                "Oferta Relâmpago: Crie promoções-relâmpago durante o dia com descontos significativos em itens selecionados.\n" +
                "Redes Sociais: Anuncie as promoções exclusivas do Dia do Consumidor nas redes sociais, incentivando os seguidores a aproveitar as ofertas e compartilhá-las com amigos."),
            CommemorativeTip("20/04/2024", "Páscoa", "Sobremesa Especial: Adicione uma sobremesa temática de Páscoa, como um sundae de chocolate com confeitos de coelho.\n" +
                "Combo de Páscoa: Ofereça um combo especial que inclua uma sobremesa de Páscoa grátis para cada lanche comprado.\n" +
                "Caça aos Ovos: Organize uma pequena 'caça aos ovos' no fast food, com prêmios para as crianças que encontrarem os ovos escondidos.\n" +
                "Decoração Temática: Decore o ambiente com coelhos e ovos de Páscoa para criar um clima festivo.\n" +
                "Redes Sociais: Publique sobre o combo especial de Páscoa e a sobremesa temática, incentivando os clientes a compartilhar suas fotos de Páscoa no fast food com uma hashtag temática."),
            CommemorativeTip("11/05/2024", "Dia das Mães", "Menu para Famílias: Crie um menu especial para famílias, com opções que agradem tanto as mães quanto os filhos.\n" +
                "Sobremesa Grátis: Ofereça uma sobremesa gratuita para todas as mães que fizerem um pedido no fast food.\n" +
                "Brinde Especial: Dê um brinde especial, como uma flor ou um cartão, para todas as mães que visitarem o fast food.\n" +
                "Combo para Compartilhar: Monte um combo familiar que inclua um lanche para cada membro da família e uma sobremesa para compartilhar.\n" +
                "Redes Sociais: Publique um vídeo ou fotos destacando o ambiente especial preparado para o Dia das Mães e incentive os clientes a compartilharem suas fotos familiares no fast food com uma hashtag dedicada."),
            CommemorativeTip("28/05/2024", "Dia do Hambúrguer", "Desconto em Hambúrgueres: Ofereça um desconto exclusivo em todos os hambúrgueres do cardápio durante o dia.\n" +
                "Hambúrguer Exclusivo: Crie um hambúrguer especial para o Dia do Hambúrguer, disponível apenas nesta data.\n" +
                "Combo do Dia: Monte um combo com hambúrguer, batata frita e bebida por um preço promocional.\n" +
                "Desafio do Hambúrguer: Lance um desafio de quem come mais hambúrgueres em um tempo limitado, com prêmios para os vencedores.\n" +
                "Redes Sociais: Anuncie o hambúrguer especial e o desafio nas redes sociais, incentivando os clientes a participar e compartilhar suas fotos usando a hashtag #DiaDoHamburguer."),
            CommemorativeTip("12/06/2024", "Dia dos Namorados", "Combo Romântico: Ofereça um combo especial para dois, incluindo dois hambúrgueres, batata frita e uma sobremesa para compartilhar.\n" +
                "Menu Especial: Crie um menu romântico com lanches temáticos, como hambúrgueres em formato de coração.\n" +
                "Brinde para Casais: Dê um brinde especial, como uma pequena sobremesa, para casais que fizerem pedidos juntos.\n" +
                "Decoração Romântica: Decore o ambiente com luzes suaves e flores para criar uma atmosfera romântica.\n" +
                "Redes Sociais: Publique fotos e vídeos do ambiente decorado e do combo romântico, e incentive os casais a compartilhar suas fotos no fast food usando uma hashtag especial."),
            CommemorativeTip("28/06/2024", "Dia do Orgulho LGBT", "Menu Colorido: Crie um menu especial com lanches inspirados nas cores da bandeira LGBT.\n" +
                "Desconto Especial: Ofereça descontos para quem vier vestido com as cores do arco-íris ou mostrar apoio à causa.\n" +
                "Evento Temático: Organize um evento ou happy hour no fast food para celebrar a diversidade e inclusão.\n" +
                "Parcerias Locais: Colabore com organizações LGBT locais para promover o evento e doar parte dos lucros para a causa.\n" +
                "Redes Sociais: Compartilhe histórias inspiradoras e mostre como o fast food apoia a comunidade LGBT, incentivando os clientes a participar do evento e compartilhar suas fotos com a hashtag #OrgulhoLGBT."),
            CommemorativeTip("30/07/2024", "Dia dos Amigos", "Promoção para Amigos: Ofereça descontos para grupos de amigos que pedirem juntos.\n" +
                "Combo Compartilhável: Crie um combo especial grande o suficiente para ser compartilhado entre amigos.\n" +
                "Atividade em Grupo: Organize uma noite de jogos ou quiz para atrair grupos de amigos ao fast food.\n" +
                "Desconto em Refil: Ofereça refil grátis para grupos de amigos que vierem ao fast food juntos.\n" +
                "Redes Sociais: Publique fotos dos grupos de amigos que visitarem o fast food e incentive-os a marcar seus amigos nas postagens, com a chance de ganhar um prêmio."),
            CommemorativeTip("10/08/2024", "Dia dos Pais", "Combo para Pais: Crie um combo especial para o Dia dos Pais, com um lanche robusto e uma sobremesa.\n" +
                "Desconto para Pais: Ofereça um desconto especial para todos os pais que vierem com seus filhos ao fast food.\n" +
                "Brinde Especial: Dê um brinde, como uma caneca ou chaveiro personalizado, para os pais que fizerem pedidos acima de um certo valor.\n" +
                "Menu para Compartilhar: Ofereça pratos ou lanches grandes que possam ser compartilhados entre pais e filhos.\n" +
                "Redes Sociais: Peça aos clientes para compartilhar fotos de seus pais no fast food e ofereça um prêmio para a foto mais criativa, usando uma hashtag dedicada ao Dia dos Pais."),
            CommemorativeTip("01/09/2024", "Semana do Brasil", "Lanches Típicos Brasileiros: Crie um hambúrguer especial ou adicione ingredientes típicos brasileiros, como queijo coalho, pimenta biquinho ou carne seca, para celebrar a cultura local.\n" +
                "Promoção Nacional: Ofereça descontos em combos com ingredientes brasileiros durante toda a Semana do Brasil.\n" +
                "Parcerias Locais: Trabalhe com fornecedores locais para destacar ingredientes frescos e nacionais no cardápio.\n" +
                "Desconto para Quem Usa Verde e Amarelo: Ofereça um desconto para clientes que vestirem as cores da bandeira brasileira.\n" +
                "Redes Sociais: Publique sobre os lanches especiais e as promoções da Semana do Brasil, incentivando os clientes a compartilhar fotos usando verde e amarelo com a hashtag #SemanaDoBrasil."),
            CommemorativeTip("15/09/2024", "Dia do Cliente", "Descontos Exclusivos: Ofereça um desconto especial para todos os clientes que visitarem o fast food nesse dia.\n" +
                "Cartão Fidelidade: Lance um cartão fidelidade onde os clientes podem acumular pontos e ganhar uma refeição gratuita.\n" +
                "Brinde para Clientes Fiéis: Dê um brinde especial para os clientes que já frequentam o fast food há um certo tempo.\n" +
                "Promoção de Indicação: Ofereça um desconto para clientes que trouxerem novos amigos para conhecer o fast food.\n" +
                "Redes Sociais: Agradeça aos clientes fiéis com uma postagem especial nas redes sociais e organize um sorteio entre aqueles que comentarem sobre sua experiência usando a hashtag #DiaDoCliente."),
            CommemorativeTip("12/10/2024", "Dia das Crianças", "Menu Infantil: Crie um menu especial para crianças, com lanches menores e brindes divertidos.\n" +
                "Brindes Infantis: Ofereça brinquedos ou itens colecionáveis com cada pedido infantil.\n" +
                "Atividades para Crianças: Organize atividades como pintura ou jogos para as crianças enquanto aguardam seus pedidos.\n" +
                "Combo Familiar: Ofereça um combo familiar que inclua opções para adultos e crianças, com preços promocionais.\n" +
                "Redes Sociais: Publique fotos dos eventos infantis no fast food e incentive os pais a compartilharem fotos dos seus filhos na loja usando uma hashtag temática como #DiaDasCrianças."),
            CommemorativeTip("31/10/2024", "Dia das Bruxas", "Decoração Assustadora: Decore o fast food com temas de Halloween, como abóboras, fantasmas e teias de aranha.\n" +
                "Lanche Temático: Crie um hambúrguer ou sobremesa especial com nomes e cores assustadoras para celebrar o Halloween.\n" +
                "Trick or Treat: Distribua doces ou brindes para crianças que vierem fantasiadas ao fast food.\n" +
                "Evento de Halloween: Organize um concurso de fantasias, com prêmios para as melhores fantasias.\n" +
                "Redes Sociais: Publique fotos das decorações e do concurso de fantasias, incentivando os clientes a compartilhar suas fotos de Halloween no fast food usando a hashtag #HalloweenFastFood."),
            CommemorativeTip("28/11/2024", "Black Friday", "Descontos Agressivos: Ofereça descontos significativos em combos e lanches durante todo o dia para atrair mais clientes.\n" +
                "Promoção de Tempo Limitado: Crie promoções relâmpago em determinados horários para incentivar a compra imediata.\n" +
                "Combo Especial: Monte um combo com preço reduzido para ser vendido apenas na Black Friday.\n" +
                "Cartão Fidelidade com Pontos Dobro: Dobre os pontos do cartão fidelidade para todas as compras feitas nesse dia.\n" +
                "Redes Sociais: Anuncie as promoções e ofertas relâmpago da Black Friday nas redes sociais, criando uma sensação de urgência e convidando os seguidores a aproveitar as ofertas usando a hashtag #BlackFridayFastFood."),
            CommemorativeTip("25/12/2024", "Natal", "Lanche de Natal: Crie um hambúrguer ou lanche especial com sabores natalinos, como molho de cranberry ou carne de peru.\n" +
                "Combo de Natal: Ofereça um combo especial que inclua uma sobremesa temática de Natal, como um sundae de panetone.\n" +
                "Decoração Natalina: Decore o fast food com luzes, árvores de Natal e ornamentos festivos para criar um ambiente aconchegante.\n" +
                "Brinde de Natal: Dê um pequeno brinde natalino, como uma mini árvore ou um cartão de Natal, para os clientes que fizerem pedidos acima de um certo valor.\n" +
                "Redes Sociais: Publique fotos do fast food decorado e do combo de Natal, e incentive os clientes a compartilhar suas experiências natalinas na loja usando a hashtag #NatalNoFastFood."),
            CommemorativeTip("31/12/2024", "Réveillon", "Combo de Fim de Ano: Ofereça um combo especial para celebrar o Réveillon, com um lanche, batata frita e uma bebida refrescante.\n" +
                "Desconto para Compras em Grupo: Ofereça um desconto para grupos que fizerem pedidos para as festas de fim de ano.\n" +
                "Brinde de Réveillon: Dê um brinde temático, como um chapéu de festa ou confetes, para quem fizer pedidos grandes.\n" +
                "Decoração de Ano Novo: Decore o ambiente com temas de Réveillon, como balões dourados e prateados.\n" +
                "Redes Sociais: Publique sobre o combo de fim de ano e as decorações de Réveillon, incentivando os clientes a compartilhar fotos de suas celebrações no fast food usando a hashtag #AnoNovoFastFood.")
        ]
        return tips_list

    @staticmethod
    def get_next_tip():
        tips_list = CommemorativeDateChecker.get_all_tips()
        today = datetime.now()
        next_tip = None

        for tip in tips_list:
            days_between = (tip.date - today).days

            if 0 <= days_between <= 30:
                if next_tip is None or tip.date < next_tip.date:
                    next_tip = tip

        if next_tip is None:
            for tip in tips_list:
                if tip.date > today:
                    if next_tip is None or tip.date < next_tip.date:
                        next_tip = tip

        return next_tip

# Exemplo de uso:
checker = CommemorativeDateChecker()
next_tip = checker.get_next_tip()
if next_tip:
    print(f"Próxima data comemorativa: {next_tip.date.strftime('%d/%m/%Y')} ({next_tip.occasion})\nDicas: {next_tip.tips}")
else:
    print("Nenhuma data comemorativa próxima.")
