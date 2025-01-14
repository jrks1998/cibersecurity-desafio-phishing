conteudo = 0

with open('/root/.set/web_clone/index.html', 'r') as f:
   conteudo = f.read()
f.close()

conteudo = conteudo.replace('<script src="https://static.xx.fbcdn.net/rsrc.php/v4/yc/r/-d_FIoNpDGV.js" data-bootloader-hash="lp6Cw4s" crossorigin="anonymous"></script>', '<!--<script src="https://static.xx.fbcdn.net/rsrc.php/v4/yc/r/-d_FIoNpDGV.js" data-bootloader-hash="lp6Cw4s" crossorigin="anonymous"></script>-->')

with open('/root/.set/web_clone/index.html', 'w') as f:
   f.write(conteudo)
f.close()