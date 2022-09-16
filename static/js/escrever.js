function autoResize()
{   var altura = window.screen.height;
    objTextArea = document.getElementById('textBody');
    var alturaArea = objTextArea.height;
    if (objTextArea.scrollHeight > objTextArea.offsetHeight)
    {
        console.log(altura);
        objTextArea.rows += 1;
        console.log("teste")
    }
}