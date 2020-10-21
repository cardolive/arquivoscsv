<p>gera o arquivo requerimentos</p>
<ul>
<li>
pip freeze > requirements.txt ()
</li>
</ul>
<p> instala as dependencias do arquivo requerimento </p>
<ul>
<li>pip install -r requirements.txt</li>
</ul>

<p>Para rodar o Flask no pronpt do windows (On Windows you need to use set instead of export):</p>
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