import { Route, Routes } from "react-router-dom";
import AllCourses from "../components/Course/AllCourses/AllCourses";
import CreateCourse from "../components/Course/CreateCourse/CreateCourse";
import EditCourse from "../components/Course/EditCourse/EditCourse";
import { Home } from "../components/Home/Home";
import Layout from "../components/Layout/Layout";
import { NotFound } from "../components/NotFound";
import AllRoomAllocations from "../components/RoomAllocation/AllRoomAllocations/AllRoomAllocations";
import CreateRoomAllocation from "../components/RoomAllocation/CreateRoomAllocation/CreateRoomAllocation";
import EditRoomAllocation from "../components/RoomAllocation/EditRoomAllocation/EditRoomAllocation";
import CreateRoutine from "../components/Routine/CreateRoutine/CreateRoutine";
import GetCourseRoutine from "../components/Routine/GetCourseRoutine/GetCourseRoutine";
import GetRoutine from "../components/Routine/GetRoutine/GetRoutine";
import AllSections from "../components/Section/AllSections/AllSections";
import AssignTeacher from "../components/Section/AssignTeacher/AssignTeacher";
import CreateSection from "../components/Section/CreateSection/CreateSection";
import EditSection from "../components/Section/EditSection/EditSection";
import AllSemesters from "../components/Semester/AllSemesters/AllSemesters";
import CreateSemester from "../components/Semester/CreateSemester/CreateSemester";
import EditSemester from "../components/Semester/EditSemester/EditSemester";
import AllTeachers from "../components/Teacher/AllTeachers/AllTeachers";
import CreateTeacher from "../components/Teacher/CreateTeacher/CreateTeacher";
import EditTeacher from "../components/Teacher/EditTeacher/EditTeacher";
import AllTimeSlots from "../components/TimeSlot/AllTimeSlots/AllTimeSlots";
import CreateTimeSlot from "../components/TimeSlot/CreateTimeSlot/CreateTimeSlot";
import EditTimeSlot from "../components/TimeSlot/EditTimeSlot/EditTimeSlot";

const AppRoutes = () => {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />

        <Route path="/routine">
          <Route path="createRoutine" element={<CreateRoutine />} />
          <Route path="teacherRoutine" element={<GetRoutine />} />
          <Route path="courseRoutine" element={<GetCourseRoutine />} />
        </Route>

        <Route path="/teacher">
          <Route path="new" element={<CreateTeacher />} />
          <Route path="all" element={<AllTeachers />} />
          <Route path="edit/:id" element={<EditTeacher />} />
        </Route>
        <Route path="/course">
          <Route path="new" element={<CreateCourse />} />
          <Route path="all" element={<AllCourses />} />
          <Route path="edit/:id" element={<EditCourse />} />
        </Route>

        <Route path="/semester">
          <Route path="new" element={<CreateSemester />} />
          <Route path="all" element={<AllSemesters />} />
          <Route path="edit/:id" element={<EditSemester />} />
        </Route>

        <Route path="/timeSlot">
          <Route path="new" element={<CreateTimeSlot />} />
          <Route path="all" element={<AllTimeSlots />} />
          <Route path="edit/:id" element={<EditTimeSlot />} />
        </Route>

        <Route path="/roomAllocation">
          <Route path="new" element={<CreateRoomAllocation />} />
          <Route path="all" element={<AllRoomAllocations />} />
          <Route path="edit/:id" element={<EditRoomAllocation />} />
        </Route>

        <Route path="/section">
          <Route path="new" element={<CreateSection />} />
          <Route path="all" element={<AllSections />} />
          <Route path="edit/:id" element={<EditSection />} />
          <Route path="assign" element={<AssignTeacher />} />
        </Route>

        <Route path="*" element={<NotFound />} />
      </Routes>
    </Layout>
  );
};

export default AppRoutes;
