import { useCallback, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import MovieDetail from "../components/MovieDetail";

function Detail() {
  const { id } = useParams();
  const [loading, setLoading] = useState(true);
  const [movie, setMovie] = useState();
  const getMovies = useCallback(async () => {
    const json = await (
      await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
    ).json();
    setMovie(json.data.movie);
    console.log(json);
    setLoading(false);
  }, [id]);
  useEffect(() => {
    getMovies();
  }, [getMovies]);
  return (
    <div>
      {loading ? (
        <strong>Loading...</strong>
      ) : (
        <div>
          <MovieDetail
            key={movie.id}
            id={movie.id}
            coverImg={movie.medium_cover_image}
            title={movie.title}
            year={movie.year}
            runtime={movie.runtime}
            genres={movie.genres}
            rating={movie.rating}
            description_full={movie.description_full}
          />
        </div>
      )}
    </div>
  );
}

export default Detail;
