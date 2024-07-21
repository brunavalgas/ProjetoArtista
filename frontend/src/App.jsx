import { useState, useEffect } from 'react';
import './index.css';

export default function App() {
  
  const [artista, setArtistas] = useState([]); // Cria um estado para armazenar os artistas
  
  useEffect(() => { // Executa a função fetchArtistas() quando o componente é montado
    fetchArtistas(); // Função para buscar os artistas
  }, []);

  async function fetchArtistas() { // Função para buscar os artistas
    const response = await fetch('http://localhost:8000/artistas/read_artistas'); // Requisição GET para a API
    const data = await response.json(); // Converte a resposta para JSON
    setArtistas(data); // Atualiza o estado com os artistas
  }

  async function createArtista(e) {
    e.preventDefault(); // Previne o comportamento padrão do formulário

    const formData = new FormData(e.target); // Cria um objeto FormData
    fetch('http://localhost:8000/artistas/create', { // Requisição POST para a API
      method: 'POST',
      body: formData // Envia o objeto FormData
    }).then(() => {
      fetchArtistas(); // Busca os artistas novamente
    })
  } 

  function deletarArtista(id) { // Função para deletar um artista
    fetch(`http://localhost:8000/artistas/delete_artista/${id}`) // Requisição DELETE para a API
    .then(() => {
      fetchArtistas(); // Busca os artistas novamente
    })
  }

  return ( // Renderiza os artistas
    <>
      <form method='POST' onSubmit={(e) => createArtista(e)}> 
        <input type="text"  name="nome_artista"  placeholder="Nome do artista" />
        <input type="text"  name="tipo_artista"  placeholder="SOLO ou BANDA" />
        <input type="text"  name="email_artista"  placeholder="Email do artista" />
        <input type="text"  name="tipo_documento"  placeholder="Tipo do Documento" />
        <input type="text"  name="numero_documento"  placeholder="Numero do Documento" />
        <button type="submit">
          Criar Artista 
        </button>
      </form>
      {artista.map((a) => ( // Mapeia os artistas
        <div>
           <h1>{a.fields.nome}</h1> 
           <h1>{a.fields.tipo}</h1>
           <h1>{a.fields.email}</h1>
           <button class="delete-button" onClick={() => deletarArtista(a.pk)}>
              Deletar
           </button>
        </div>
        ))}
    </>
  )
}