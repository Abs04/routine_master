import { Loader } from "lucide-react";
import { useParams } from "react-router-dom";
import { useGetSectionQuery } from "../../../features/section/sectionApi";
import EditSectionForm from "./EditSectionForm";

const EditSection = () => {
  const { id } = useParams();

  const { data, isLoading, isError } = useGetSectionQuery(id);

  return (
    <section className="py-8">
      <div className="container mx-auto px-2">
        <div className="p-4 border rounded bg-gray-100 mt-4">
          <div>
            <h2>Edit Section</h2>
          </div>
          {isLoading && <Loader />}
          {!isError && !isLoading && data && <EditSectionForm data={data} />}
        </div>
      </div>
      <div></div>
    </section>
  );
};

export default EditSection;
