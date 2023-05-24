import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
// 상태 관리, 전역 변수 관리, 컴포넌트간 데이터 공유
import {
  RecoilRoot,
  atom,
  useRecoilState,
  useRecoilValue,
  selector,
} from "recoil";

// useEffect 없이 API 통신이 가능하도록
import { QueryClient, QueryClientProvider, useQuery } from "react-query";

const root = ReactDOM.createRoot(document.getElementById("root"));

const queryClient = new QueryClient();

root.render(
  <React.StrictMode>
    <RecoilRoot>
      <QueryClientProvider client={queryClient}>
        <App />
      </QueryClientProvider>
    </RecoilRoot>
  </React.StrictMode>,
  document.getElementById("root")
);
