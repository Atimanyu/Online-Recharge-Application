import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./App.css";
import Home from "./Components/Home/Home";
import Login from "./Components/Login/Login";
import Prepaid from "./Components/Prepaid/Prepaid";
import RechargeHistoryTable from "./Components/History/History";
import ProfileUpdate from "./Components/Profile-Updation/Profile";
import AdminPage from "./Components/Admin/admin";

const r = createBrowserRouter([
  {
    path: "/",
    element: <Login />,
  },
  {
    path: "/home",
    element: <Home />,
    children: [{ path: "prepaid", element: <Prepaid /> }],
  },
  { path: "/history", element: <RechargeHistoryTable /> },
  { path: "/profile/update", element: <ProfileUpdate /> },
  {path: "/admin", element:<AdminPage/>}
]);
function App() {
  return <RouterProvider router={r} />;
}

export default App;
