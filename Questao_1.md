## Questão 1

Eu analisaria isso em duas etapas, porque são problemas diferentes. Um é como o site carrega e o outro é como ele me enxerga.

### Primeira etapa.
O Requests só baixa o esqueleto do site. Se a tabela demora 2 segundos, é quase uma certeza que ela é carregada por um script depois que a página já abriu. O Requests não espera esse tempo e nem executa código JS, por isso ele não 'vê' a tabela.
Eu abriria o navegador, apertaria F12 e iria na aba Network. Ao apertar F5, eu iria ver se aparece alguma requisição de arquivo JSON ou algo do tipo. Se eu achar o link direto de onde os dados vêm, eu tento usar o Requests direto nesse link, porque o dado já vem limpo. 
Se não tiver um link fácil, eu trocaria o Requests pelo Selenium. Eu usaria uma função wait_for_selector, que diz ao script, 'Só tenta ler a tabela quando ela realmente aparecer na tela'.

### Segunda etapa.

O erro 403 acontece porque o acesso é mecânico demais. Eu usaria o random e o numpy para criar um comportamento humano.

Em vez de um tempo fixo, eu usaria time.sleep(random.uniform(1, 5)) entre as páginas.

Com o numpy, eu poderia até simular uma 'curva normal' de acessos, fazendo com que o script não pareça um metrônomo, mas sim alguém navegando com tempos variados.

Assim que o Playwright (ou Selenium) conseguir 'esperar' os 2 segundos e capturar a tabela, eu passaria o HTML direto para o Pandas.