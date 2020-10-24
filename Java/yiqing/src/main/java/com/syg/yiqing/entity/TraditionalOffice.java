package com.syg.yiqing.entity;

import javax.persistence.*;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "traditional_office")
public class TraditionalOffice {

    @Id // 该字段对应数据库中的列为主键
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 主键自增长
    @Column(name = "id") // 对应tradition_office表中的id列
    private Integer id;

    @Column(name = "name")
    private String name;

    @Column(name = "city")
    private String city;

    @Column(name = "area")
    private String area;

    @Column(name = "address")
    private String address;

    @Column(name = "completion_time")
    private String completion_time;

    @Column(name = "floor_number")
    private Integer floor_number;

    @Column(name = "floor_height")
    private Float floor_height;

    @Column(name = "office_owner")
    private String office_owner;

    @Column(name = "property_company")
    private String property_company;

    @Column(name = "peoelv_number")
    private Integer peoelv_number;

    @Column(name = "freelv_number")
    private Integer freelv_number;

    @Column(name = "open_time")
    private Integer open_time;

    @Column(name = "height")
    private Float height;


}
