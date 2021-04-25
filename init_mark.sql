use stu_info;

create table polls_studentmark(
	mark_id varchar(20),
	stu_id varchar(20),
	stu_name varchar(20),
    course_id varchar(50),
    assignment_1 varchar(20),
    assignment_2 varchar(20),
    assignment_3 varchar(20),
    assignment_4 varchar(20),
    assignment_5 varchar(20),
    assignment_6 varchar(20)
    
    
    
    );
    
use stu_info;
INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('001','001', 'AndyXia', 'csc3170', '100','100', '100','100', '100','100');
INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('002','001', 'AndyXia', 'csc4150', '100','100', '100','100', '100','100');
INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('003','001', 'AndyXia', 'csc4008', '100','100', '100','100', '100','100');
INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('004','001', 'AndyXia', 'mat3007', '100','100', '100','100', '100','100');


INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('005','002', 'DodoXia', 'csc3170', '100','100', '100','100', '100','100');
INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('006','002', 'DodoXia', 'csc4150', '100','100', '100','100', '100','100');
INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('007','002', 'DodoXia', 'eco2011', '100','100', '100','100', '100','100');

INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('008','003', 'AlexLi', 'csc3170', '100','100', '100','100', '100','100');
INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('009','003', 'AlexLi', 'csc4001', '100','100', '100','100', '100','100');

INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('010','004', 'ArthurLi', 'csc3170', '100','100', '100','100', '100','100');
INSERT INTO `stu_info`.`polls_studentmark` (`mark_id`,`stu_id`, `stu_name`, `course_id`, `assignment_1`, `assignment_2`, `assignment_3`, `assignment_4`, `assignment_5`, `assignment_6`) VALUES ('011','004', 'ArthurLi', 'csc4001', '100','100', '100','100', '100','100');


select * from polls_studentmark;


