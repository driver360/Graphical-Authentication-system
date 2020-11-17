def update(self):
    db = ob.database()
    query = "update registration_table set name = %s,email = %s,contact = %s,question =%s,answer =%s,p1 = %s,p2 = %s, p3 = %s where email ="+self.R_email_var.get()
    val = (self.R_name_var.get(),self.R_email_var.get(),self.R_contact_var.get(),self.R_question_var.get(),self.R_answer_var.get(),self.R_path_list_var[0],self.R_path_list_var[1],self.R_path_list_var[2])
    is_success = ob.universal_Transact(query, val)
    if is_success == 1:
        print("Done")
    else:
        print("Not done")