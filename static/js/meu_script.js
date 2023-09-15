$(document).ready(function() {
    var socket = io("localhost:5000");
    socket.on("connect", function() {
        console.log("Usuário conectou");
    });

    socket.on("message", function(data) {
        console.log("Disparou uma mensagem");
        $("#lista_mensagens").append($("<p>").text(data));
        // Scroll to the bottom of the chat container
        $("#lista_mensagens").scrollTop($("#lista_mensagens")[0].scrollHeight);
    });

    $("#botao").on("click", function() {
        console.log("Clicou no botão");
        socket.send($("#usuario").val() + ": " + $("#mensagem").val());
        $("#mensagem").val("");
    });
    // Para o caso do usuário da "enter" ao invés do clique
    $("#mensagem").on('keypress', function() {
        if (event.key === "Enter") {
            console.log("deu enter");
            socket.send($('#usuario').val() + ": " + $('#mensagem').val());
            $('#mensagem').val('');
        }
    });
});
