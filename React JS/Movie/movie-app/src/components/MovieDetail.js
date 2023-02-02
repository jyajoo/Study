import PropTypes from "prop-types";

function MovieDetail({
  id,
  coverImg,
  title,
  year,
  runtime,
  genres,
  rating,
  description_full,
}) {
  return (
    <div>
      <img src={coverImg} alt={title} />
      <h2>{title}</h2>
      <p>{year}</p>
      <p>runtime : {runtime}</p>
      <p>rating : {rating}</p>
      <ul>
        {genres.map((genre) => (
          <li key={genre}>{genre}</li>
        ))}
      </ul>
      <p>{description_full}</p>
    </div>
  );
}

MovieDetail.propTypes = {
  id: PropTypes.number.isRequired,
  coverImg: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  genres: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default MovieDetail;
