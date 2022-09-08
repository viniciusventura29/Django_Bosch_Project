function autoResize()
{
    objTextArea = document.getElementById('body');
    while (objTextArea.scrollHeight > objTextArea.offsetHeight)
    {
        objTextArea.rows += 1;
    }
}