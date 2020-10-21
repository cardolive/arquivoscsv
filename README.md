<h1>gera o arquivo requerimentos</h1>
<ul>
<li>
    pip freeze > requirements.txt ()
</li>
</ul>
<p> instala as dependencias do arquivo requerimento </p>
<ul>
<li>pip install -r requirements.txt</li>
</ul>
<hr>
<h2>Para rodar o Flask no pronpt do windows (On Windows you need to use set instead of export):</h2>
<ul>
<li> set FLASK_APP=app/app.py </li>
<li> set FLASK_ENV=development </li>
<li>flask run</li>
</ul>
<h5>  Resposta: </h5>
<ul>
 <li> Serving Flask app "app.py" (lazy loading)</li>
 <li> Environment: development</li>
 <li> Debug mode: on</li>
 <li> Restarting with stat</li>
 <li> Debugger is active!</li>
 <li> Debugger PIN: 999-999-999</li>
 <li> Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</li>
</ul>
<hr>
<h2>Contextos</h2>
<ul>
    <li>contexto de confirguração </li>
    <ul>
        <li>alterações antes de iniciar a app, ex: dentro do create_app</li>
        <li>current_app</li>
    </ul>
    <li>contexto de aplicação </li>
    <ul>
        <li>quando roda a app (flask run)</li>
        <li>testes</li>
        <li>hooks </li>
    </ul>
    <li>contexto do request (views)</li>
    <ul>
        <li>quando existe um get/post na app rodando</li>
        <li>request, session</li>
    </ul>
</ul>
<hr>
<h3>version = "0.1.0" # major, minor, patch (sequencia da versão)</h3>

<h2>Dado um número de versão MAJOR.MINOR.PATCH, incremente a:</h2>
<ul>
    <li>versão Maior(MAJOR): quando fizer mudanças incompatíveis na API,</li>
    <li>versão Menor(MINOR): quando adicionar funcionalidades mantendo compatibilidade, e</li>
    <li>versão de Correção(PATCH): quando corrigir falhas mantendo compatibilidade.</li>
</ul>
<p>Rótulos adicionais para pré-lançamento(pre-release) e metadados de construção(build) estão disponíveis como extensão ao formato MAJOR.MINOR.PATCH.</p>
<p>https://semver.org/lang/pt-BR/</p>