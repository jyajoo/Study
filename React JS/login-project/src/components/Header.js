import { NavLink } from "react-router-dom";

function Header() {
  return (
    <ul className="flex shadow">
      <li>
        <NavLink to="/home/main">홈</NavLink>
      </li>
      <li>
        <NavLink to="/account/login">로그인</NavLink>
      </li>
    </ul>
  );
}

export default Header;
